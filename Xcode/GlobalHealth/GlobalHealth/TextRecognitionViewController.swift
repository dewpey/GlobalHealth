import UIKit
import Speech
import SocketIO
import AVFoundation
import Starscream
import SwiftyJSON
import Alamofire
import ROGoogleTranslate
import AZDialogView

class TextRecognitionViewController: UIViewController, SFSpeechRecognizerDelegate, WebSocketDelegate {

    var voiceInput = ""
    var language = "en"
    //var params = ROGoogleTranslateParams(
    //text:   "Here you can add your sentence you want to be translated")
    
    //let translator = ROGoogleTranslate(with: "API Key here")
    
        var socket: WebSocket!
    
    func websocketDidConnect(socket: WebSocketClient) {
        print("websocket is connected")
    }
    
    func websocketDidDisconnect(socket: WebSocketClient, error: Error?) {
        if let e = error as? WSError {
            print("websocket is disconnected: \(e.message)")
        } else if let e = error {
            print("websocket is disconnected: \(e.localizedDescription)")
        } else {
            print("websocket disconnected")
        }
    }
    
    func websocketDidReceiveMessage(socket: WebSocketClient, text: String) {
        print("Received text: \(text)")
        recLabel.text = text
        
        let translator = ROGoogleTranslate()
        translator.apiKey = "AIzaSyBXojFDvT_g2FsdAQeh3TSZYgwbLmy2WDk" // Add your API Key here
        if(language != "en"){
        var params = ROGoogleTranslateParams(source: "en",
                                             target: self.language,
                                             text:   text)
        
        translator.translate(params: params) { (result) in
            print("Translation: \(result)")
            self.speak(words: result, language: self.language)
        }
        }else{
            self.speak(words: text, language: self.language)
        }
      
        
    }
    
    func websocketDidReceiveData(socket: WebSocketClient, data: Data) {
        print("Received data: \(data.count)")
        
    }
    
    
    @IBOutlet weak var recLabel: UILabel!
    @IBOutlet weak var microphoneButton: UIButton!
    @IBOutlet weak var sendingLabel: UILabel!
    
    var speechRecognizer = SFSpeechRecognizer(locale: Locale.init(identifier: "en"))!
    
    private var recognitionRequest: SFSpeechAudioBufferRecognitionRequest?
    private var recognitionTask: SFSpeechRecognitionTask?
    private let audioEngine = AVAudioEngine()
    
    
    let speechSynthesizer = AVSpeechSynthesizer()
    
    override func viewDidLoad() {
        
        super.viewDidLoad()
        
        var request = URLRequest(url: URL(string: "ws://globalhealth-blurjoe.c9users.io:8080?language=en")!)
        request.timeoutInterval = 5
        socket = WebSocket(request: request)
        socket.delegate = self
        socket.connect()
        
        microphoneButton.isEnabled = false
        
        speechRecognizer.delegate = self
        
        SFSpeechRecognizer.requestAuthorization { (authStatus) in
            
            var isButtonEnabled = false
            
            switch authStatus {
            case .authorized:
                isButtonEnabled = true
                
            case .denied:
                isButtonEnabled = false
                print("User denied access to speech recognition")
                
            case .restricted:
                isButtonEnabled = false
                print("Speech recognition restricted on this device")
                
            case .notDetermined:
                isButtonEnabled = false
                print("Speech recognition not yet authorized")
            }
            
            OperationQueue.main.addOperation() {
                self.microphoneButton.isEnabled = isButtonEnabled
            }
        }
    }
    
    @IBAction func microphoneTapped(_ sender: AnyObject) {
        //speak(words: "hello");
        if audioEngine.isRunning {
            audioEngine.stop()
            recognitionRequest?.endAudio()
            microphoneButton.isEnabled = false
        } else {
            startRecording()
        }
    }
    
    func startRecording() {
        
        var timer = Timer.scheduledTimer(timeInterval: 1, target: self, selector: #selector(sendData), userInfo: nil, repeats: false)
        
        

        
        //
        
        
        if recognitionTask != nil {  //1
            recognitionTask?.cancel()
            recognitionTask = nil
        }
        
        let audioSession = AVAudioSession.sharedInstance()  //2
        do {
            try audioSession.setCategory(AVAudioSession.Category.playAndRecord, mode: .measurement)
             try audioSession.setCategory(AVAudioSession.Category.playAndRecord, mode: .measurement, options: .defaultToSpeaker)
            try audioSession.setActive(true, options: .notifyOthersOnDeactivation)
        } catch {
            print("audioSession properties weren't set because of an error.")
        }
        
        recognitionRequest = SFSpeechAudioBufferRecognitionRequest()  //3
        
        let inputNode = audioEngine.inputNode
        
        guard let recognitionRequest = recognitionRequest else {
            fatalError("Unable to create an SFSpeechAudioBufferRecognitionRequest object")
        } //5
        
        recognitionRequest.shouldReportPartialResults = true  //6
        
        
        recognitionTask = speechRecognizer.recognitionTask(with: recognitionRequest, resultHandler: { (result, error) in  //7
            
            timer.invalidate()
            timer = Timer.scheduledTimer(timeInterval: 0.8, target: self, selector: #selector(self.sendData), userInfo: nil, repeats: false)
            
            
            var isFinal = false  //8
            if result != nil {
                
                var formattedResult = result?.bestTranscription.formattedString
                let word = result?.bestTranscription.segments[(result?.bestTranscription.segments.count)!-1 ?? 0].substring
                
                print(word)
                
                //self.socket.write(string: formattedResult!)
                
                self.voiceInput = formattedResult ?? ""
                self.sendingLabel.text = formattedResult
                
                //9
                isFinal = (result?.isFinal)!

            }
            
            if error != nil || isFinal {  //10
                self.audioEngine.stop()
                inputNode.removeTap(onBus: 0)
                
                self.recognitionRequest = nil
                self.recognitionTask = nil
                
                self.microphoneButton.isEnabled = true
            }
        })
        
        let recordingFormat = inputNode.outputFormat(forBus: 0)  //11
        inputNode.installTap(onBus: 0, bufferSize: 1024, format: recordingFormat) { (buffer, when) in
            self.recognitionRequest?.append(buffer)
        }
        
        audioEngine.prepare()  //12
        
        do {
            try audioEngine.start()
        } catch {
            print("audioEngine couldn't start because of an error.")
        }
        
        sendingLabel.text = "Say something, I'm listening!"
        
    }
    
    func speechRecognizer(_ speechRecognizer: SFSpeechRecognizer, availabilityDidChange available: Bool) {
        if available {
            microphoneButton.isEnabled = true
        } else {
            microphoneButton.isEnabled = false
        }
    }
    
    func speak(words: String, language: String){
        let utterance = AVSpeechUtterance(string: words)
        utterance.voice = AVSpeechSynthesisVoice(language: language)
        //speechUtterance.rate = 0.5
        //speechUtterance.pitchMultiplier = 0.25
        utterance.volume = 1
        
        speechSynthesizer.speak(utterance)
    }
    
    @IBAction func openLanguageDialog(_ sender: Any) {
        let dialog = AZDialogViewController(title: "Languages", message: "Choose your language")
        dialog.addAction(AZDialogAction(title: "English") { (dialog) -> (Void) in
            self.language = "en"
            self.speechRecognizer = SFSpeechRecognizer(locale: Locale.init(identifier: "en"))!
            dialog.dismiss()
        })
        
        dialog.addAction(AZDialogAction(title: "Spanish") { (dialog) -> (Void) in
            self.language = "es"
            self.speechRecognizer = SFSpeechRecognizer(locale: Locale.init(identifier: "es"))!
            dialog.dismiss()
        })
        
        dialog.addAction(AZDialogAction(title: "Chinese (Simplified)") { (dialog) -> (Void) in
            self.language = "zh-CN"
            self.speechRecognizer = SFSpeechRecognizer(locale: Locale.init(identifier: "zh-CN"))!
            dialog.dismiss()
        })
        
        dialog.addAction(AZDialogAction(title: "Chinese (Traditional)") { (dialog) -> (Void) in
            self.language = "zh-TW"
            self.speechRecognizer = SFSpeechRecognizer(locale: Locale.init(identifier: "zh-TW"))!
            dialog.dismiss()
        })
        
        
        dialog.addAction(AZDialogAction(title: "Hindi") { (dialog) -> (Void) in
            self.language = "hi"
            self.speechRecognizer = SFSpeechRecognizer(locale: Locale.init(identifier: "hi"))!
            dialog.dismiss()
        })
        dialog.addAction(AZDialogAction(title: "Arabic") { (dialog) -> (Void) in
            self.speechRecognizer = SFSpeechRecognizer(locale: Locale.init(identifier: "ar"))!
            self.language = "ar"
            dialog.dismiss()
        })
        dialog.show(in: self)
    }
    
    var previous = ""
    
    @objc func sendData(){
        
        print(voiceInput)
        print("previous \(previous)")
        let replaced = voiceInput.replacingOccurrences(of: previous, with: "")
        print(replaced)
        self.socket.write(string: replaced)
        //audioEngine.reset()
        previous = voiceInput;
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        audioEngine.stop()
    }
    
}

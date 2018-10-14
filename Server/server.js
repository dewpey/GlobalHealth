// server.js

// BASE SETUP
// =============================================================================

// call the packages we need
var sleep = require('sleep');
var express    = require('express');        // call express
var app        = express();                 // define our app using express
var bodyParser = require('body-parser');
const VoiceResponse = require('twilio').twiml.VoiceResponse;
// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const accountSid = 'AC8ee6b7eab8455e48d74a5b5378fd21e9';
const authToken = '0a07c546a4b0a5c9634531509e154d23';
const client = require('twilio')(accountSid, authToken);


var port = process.env.PORT || 8080;        // set our port

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router();              // get an instance of the express Router

var words = ""

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/', function(req, res) {
    const response = new VoiceResponse();
    const gather = response.gather({
    input: 'speech',
    action: '/partialResultCallback',
    partialResultCallback: '/partialResultCallback',
    language: 'es-MX'
});
    //assign conference rooms (maybe based on phone number)
    //dial.conference('Room 1234');
    //callSender('973-932-8343','573-263-3622');
    //returns to twilio
    res.send(response.toString());
    console.log(response.toString());
    
});

router.get('/partialResultCallback', function(req, res) {
    console.log(req);
});

router.post('/partialResultCallback', function(req, res) {
    console.log(req.body.UnstableSpeechResult);
    words += " " + req.body.UnstableSpeechResult;
});

router.get('/triggerCall', function(req, res){
    let from = req.query.from;
    let to = req.query.to;
    console.log(to);
    console.log(from);
    callSender(to,from);
    //callReciever(to);
});

router.get('/recieverCall', function(req, res){

        const VoiceResponse = require('twilio').twiml.VoiceResponse;
        const response = new VoiceResponse();
        
        for(var i = 0; i<100; i++){
            response.say({
             voice: 'woman',
             language: 'es',
            },
            words
            );
            
            response.pause({
                length: 1
            });
        }

    
res.send(response.toString());
console.log(response.toString());
});

function callSender(to,from){
    client.calls
      .create({
         url: 'http://demo.twilio.com/docs/voice.xml',
         to: to,
         from: from
       })
      .then(call => console.log(call.sid))
      .done();
      
}

function callReciever(to){
    const response = new VoiceResponse();
const dial = response.dial();
    response.dial(to);
}

// more routes for our API will happen here

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);
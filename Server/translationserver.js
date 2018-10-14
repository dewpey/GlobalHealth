const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

var googleTranslate = require('google-translate')('AIzaSyBXojFDvT_g2FsdAQeh3TSZYgwbLmy2WDk');

wss.on('connection', function connection(ws,req) {
  
  ws.on('message', function incoming(message) {
    googleTranslate.translate(message, 'en', function(err, translation) {
    console.log(translation.translatedText);
      wss.clients.forEach(function each(client) {
        console.log(client)
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(translation.translatedText);
      }
    });
  });
    

  });

  ws.send('The call is now ready');
  
  
});

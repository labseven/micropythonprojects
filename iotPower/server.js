PORT = 4444;

const server = require('net').createServer((socket) => {
  console.log("connected");
  socket.setEncoding('utf8');
  socket.setNoDelay();


  socket.on('data', (data) => { console.log(data); });

  setInterval(() => {
    sendValue(socket);
  }, 1000);
}).listen(PORT);


function sendValue(socket) {
  value = (Date.now()%2).toString();
  console.log('sending', value);
  socket.write(value);
}

console.log('server running on', PORT);

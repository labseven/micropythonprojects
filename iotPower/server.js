PORT = 4444;

const server = require('net').createServer((socket) => {
  console.log("connected");
  socket.setEncoding('utf8');
  socket.setNoDelay();


  socket.on('data', (data) => {
    lines = data.split('\n');

    if (lines[0][0] === 'G'){
      console.log('Get request');
      socket.write('<html><p>Hi<\\p><\\html>');
      socket.end();
    } else {
      console.log(lines[0]);
      console.log(data);
      setInterval(() => {
        sendValue(socket);
      }, 1000);
    }

  });

  socket.on('end', (data) => {
    console.log('END!!!');
  });
}).listen(PORT);

function sendValue(socket) {
  value = (Date.now()%2).toString();
  console.log('sending', value);
  socket.write(value);
  // socket.end();
}

console.log('server running on', PORT);

PORT = 80;

const express    = require('express');
const app        = express();

const http = require('http').Server(app);


app.get('/*', sendHi);
app.get('/', sendHi);

app.post('/upvote', function (req, res) {
  console.log('upvoted');
  res.send('successful upvote');
})

function sendHi(req, res) {
  // res.redirect(307, 'https://futureboard.olin.build');
  res.send('Hi')
}


http.listen(PORT);
console.log('server running on', PORT);

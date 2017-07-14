require('net').createServer(function (socket) {
    console.log("connected");

    socket.write('hi');

    socket.on('data', function (data) {
        console.log(data.toString());
    });

    socket.end();
})

.listen(1444);



console.log('running server');

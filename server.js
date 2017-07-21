require('net').createServer(function (socket) {
    console.log("connected");

    socket.write('hi');

    socket.on('data', function (data) {
        console.log(data.toString());
    });

    // socket.end();
})

.listen(80);



console.log('running server');

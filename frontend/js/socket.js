var server = new WebSocket('ws://localhost:10000');

server.onclose = function () {
    console.log('socket onclose');
    $('#status').text("Socket is closed");
    $('#ready_state').text("Ready state: " + server.readyState)
}

server.onerror = function () {
    console.log('socket onerror');
    $('#status').text("Socket has error");
    $('#ready_state').text("Ready state: " + server.readyState)
}

server.onmessage = function (e) {
    console.log('socket onmessage');
    console.log(e.data);
    $('#status').text("Socket received message");
    $('#ready_state').text("Ready state: " + server.readyState)
}

server.onopen = function () {
    console.log('socket onopen');
    $('#status').text("Socket is open");
    $('#ready_state').text("Ready state: " + server.readyState)
}
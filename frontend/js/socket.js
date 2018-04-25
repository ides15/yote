// Creating a WebSocket instance
var server = new WebSocket('ws://localhost:10000');

// When the socket is connected to the socket server,
// the socket will send the server the session_url that
// is connected.
server.onopen = function () {
    $('#status').text("Socket is open");
    $('#ready_state').text("Ready state: " + server.readyState)
    server.send(JSON.stringify({
        session_url: localStorage.getItem('session_url'),
    }));
}

// When the socket receives a message from the server,
// the message will be parsed as JSON.
server.onmessage = function (e) {
    $('#ready_state').text("Ready state: " + server.readyState);

    var res = JSON.parse(e.data);

    // If the message is a list of connections on the server,
    // the list of connections will be updated with the current
    // connections.
    if (res.connections) {
        var connections_list = $('#connections_list');
        connections_list.empty();

        $.each(res.connections, function (index, element) {
            var li = $('<li class="connection"/>').text(element);
            li.appendTo(connections_list);
        });

        return;
    }

    // If the session_url of the client sending the incoming message 
    // is the same session_url as the currently connected client,
    // reflect the change as described in the incoming "change" object.
    if (res.session_url == localStorage.getItem('session_url')) {
        var replacement = res.text;
        var from = res.from;
        var to = res.to;
        var origin = res.origin;

        if (res.origin == "+delete") {
            editor.getDoc().replaceRange(replacement, from, to);
        } else {
            editor.getDoc().replaceRange(replacement, from, to, origin);
        }

        // Handles the code style indentaion
        editor.indentLine(to.line, "smart");
    }
}

server.onerror = function () {
    $('#status').text("Socket has error");
    $('#ready_state').text("Ready state: " + server.readyState)
}

server.onclose = function () {
    $('#status').text("Socket is closed");
    $('#ready_state').text("Ready state: " + server.readyState)
}
var server = new WebSocket('ws://localhost:10000');

server.onclose = function () {
    $('#status').text("Socket is closed");
    $('#ready_state').text("Ready state: " + server.readyState)
}

server.onerror = function () {
    $('#status').text("Socket has error");
    $('#ready_state').text("Ready state: " + server.readyState)
}

server.onmessage = function (e) {
    $('#ready_state').text("Ready state: " + server.readyState);

    var res = JSON.parse(e.data);

    var replacement = res.text;
    var from = res.from;
    var to = res.to;
    var origin = res.origin;

    if (res.origin == "+delete") {
        editor.getDoc().replaceRange(replacement, from, to);
    } else {
        editor.getDoc().replaceRange(replacement, from, to, origin);
    }
}

server.onopen = function () {
    $('#status').text("Socket is open");
    $('#ready_state').text("Ready state: " + server.readyState)
}
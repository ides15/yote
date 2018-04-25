var server = new WebSocket('ws://localhost:10000');

server.onopen = function () {
    $('#status').text("Socket is open");
    $('#ready_state').text("Ready state: " + server.readyState)
    server.send(JSON.stringify({
        session_url: localStorage.getItem('session_url'),
    }));
}

server.onmessage = function (e) {
    $('#ready_state').text("Ready state: " + server.readyState);

    var res = JSON.parse(e.data);

    if (res.connections) {
        var connections_list = $('#connections_list');
        connections_list.empty();

        $.each(res.connections, function (index, element) {
            var li = $('<li class="connection"/>').text(element);
            li.appendTo(connections_list);
        });

        return;
    }

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
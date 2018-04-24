var config = {
    value: "",
    mode: "javascript",
    theme: "material",
    indentUnit: 4,
    indentWithTabs: true,
    lineNumbers: true
};

editorPosition = document.getElementById("main");

var editor = CodeMirror(editorPosition, config);

editor.on("inputRead", function (cm, change) {
    server.send(JSON.stringify(change));
});

editor.on("change", function (cm, change) {
    if (change.origin === "+delete") {
        server.send(JSON.stringify(change));
    }
});

editor.on("keyHandled", function (cm, name, e) {
    var cursor = editor.getDoc().getCursor();

    if (name === "Enter") {
        server.send(JSON.stringify({
            text: "\n",
            from: cursor,
            to: cursor,
        }));
    } else if (name === "Tab") {
        server.send(JSON.stringify({
            text: "\t",
            from: cursor,
            to: cursor,
        }));
    }
});
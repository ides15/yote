var config = {
    value: "",
    mode: "javascript",
    theme: "material",
    indentUnit: 4,
    lineNumbers: true
};

editorPosition = document.getElementById("main");

var editor = CodeMirror(editorPosition, config);

editor.on("inputRead", function (cm, change) {
    server.send(JSON.stringify(change));
});

editor.on("change", function(cm, change) {
    if (change.origin === "+delete") {
        server.send(JSON.stringify(change));
    }
});
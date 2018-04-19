var config = {
    value: "",
    mode: "javascript",
    theme: "material",
    indentUnit: 4,
    lineNumbers: true
};

var editor = CodeMirror(document.getElementById("main"), config);
var objToSend = {};

editor.on("change", function(e, change) {
    console.log(change);
    server.send(JSON.stringify(change));
});

editor.on("cursorActivity", function(e) {
    console.log(editor.getCursor());
});
// configuration options for the editor,
// using JavaScript syntax highlighting,
// material theme, etc.
var config = {
    value: "",
    mode: "javascript",
    theme: "material",
    indentUnit: 4,
    indentWithTabs: true,
    lineNumbers: true
};

// appending the editor to the main page
editorPosition = document.getElementById("main");

// calling CodeMirror constructor to set editor in page
var editor = CodeMirror(editorPosition, config);

// instead of onchange, inputRead only fires 
// when the user physically types characters into
// the editor. onchange, on the other hand, will be
// called whenever any change is made to the editor,
// including when the editor is updated with any other
// clients involved in the session. This will cause an 
// infinite loop of change events to be called and will
// corrupt the editor's state.
editor.on("inputRead", function (cm, change) {
    // sending the session URL and the change event object to the server
    server.send(JSON.stringify(Object.assign({
        session_url: localStorage.getItem('session_url'),
    }, change)));
});

// using the onchange event for whenever a deletion event happens.
// This sends the delete change event to the server and it is in turn 
// broadcasted to the other clients in that session.
editor.on("change", function (cm, change) {
    if (change.origin === "+delete") {
        server.send(JSON.stringify(Object.assign({
            session_url: localStorage.getItem('session_url'),
        }, change)));
    }
});

// Using the keyHandled event to handle LF/CRLF and tab events. 
// Basically sends a "change" object (like the handlers above)
// to the server and again is broadcasted to the other clients.
editor.on("keyHandled", function (cm, name, e) {
    var cursor = editor.getDoc().getCursor();

    if (name === "Enter") {
        server.send(JSON.stringify({
            text: "\n",
            from: cursor,
            to: cursor,
            session_url: localStorage.getItem('session_url'),
        }));
    } else if (name === "Tab") {
        server.send(JSON.stringify({
            text: "\t",
            from: cursor,
            to: cursor,
            session_url: localStorage.getItem('session_url'),
        }));
    }
});
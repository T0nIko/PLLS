var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
    mode: {
        name: "python",
        version: 3,
        singleLineStringErrors: false
    },
    lineNumbers: true,
    lineWrapping: true,
    indentUnit: 4,
    matchBrackets: true
});
//TODO: fix editor size scaling
editor.setSize(document.innerWidth * 0.7, 500);

var pending;

editor.on("change", function () {
    clearTimeout(pending);
    pending = setTimeout(update, 400);
});

function looksLikeCpp(code) {
    return /^\s*\(\s*{\b/.test(code) && /^\s*[;\(]/.test(code);
}

function update() {
    editor.setOption("mode", looksLikeCpp(editor.getValue()) ? "python" : "text/x-c++src");
}

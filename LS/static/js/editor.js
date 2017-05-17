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

editor.setSize(window.innerWidth * 0.45, window.innerHeight * 0.65);

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

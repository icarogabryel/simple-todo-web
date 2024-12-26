function editText() {
    const textDisplay = document.getElementById("textDisplay")

    if (textDisplay.isContentEditable) {
        textDisplay.contentEditable = "false";
        textDisplay.style.border = "1px solid #ccc";
    } else {
        textDisplay.contentEditable = "true";
        textDisplay.style.border = "2px solid #007bff";
        textDisplay.focus();
    }
}

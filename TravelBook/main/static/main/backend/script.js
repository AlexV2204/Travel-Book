let value = false;

function menu() {
    var elem = document.getElementById("menu");
    if (value == false) {
        elem.style.position = "static";
        elem.style.visibility = "visible";
        value = true;
    } else {
        elem.style.position = "absolute";
        elem.style.visibility = "hidden";
        value = false;
    }
}
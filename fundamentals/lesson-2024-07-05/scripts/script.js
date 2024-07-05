
function changeContent() {
    document.getElementById("greet").innerHTML = "Welcome to Python course!";

}


function validateInput() {
    var input = document.getElementById("numInput").value;
    var msg = ""

    if (input > 100 || input < 1) {
        msg = "You input number is out of range.";
    } else {
        msg = "You entered a number " + input + "."
    }

    document.getElementById("message").innerHTML = msg

}

function displayTime() {

}

function gamePlay() {

}

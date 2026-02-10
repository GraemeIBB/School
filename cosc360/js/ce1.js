window.addEventListener("DOMContentLoaded", (event) => {
    const form = document.querySelector("#form").addEventListener("submit", (e) => {
        const fieldValue = document.querySelector("#username").value;
        const errMsg = document.querySelector("#error_msg")
        if (fieldValue == null || fieldValue == "") {
            //field was empty, prevent submit
            e.preventDefault();
            errMsg.innerHTML = "Enter a username"
            errMsg.style.color = "red";
        } else {
            errMsg.innerHTML = "";
            errMsg.style.color = "black";

        }

    })
})

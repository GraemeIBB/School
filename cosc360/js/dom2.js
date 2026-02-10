const text = document.createTextNode("this is dynamic");
const p = document.createElement("p");

p.appendChild(text);
window.addEventListener("DOMContentLoaded", (event) => {
    const container = document.getElementById("container");
    container.appendChild(p);
    container.addEventListener("click", (event) => {
        let a = Math.floor(Math.random() * 255).toString(16);
        let b = Math.floor(Math.random() * 255).toString(16);
        let c = Math.floor(Math.random() * 255).toString(16);
        container.style.backgroundColor = `#${a}${b}${c}`;
    })

    //Example of a general event listener placed on elements with id 'loginForm'
    document.querySelector("#loginForm").addEventListener("submit", (e) => {
        let pass = document.querySelector("#pw").value;
        if (pass == "") {
            alert("enter a password")
            e.preventDefault();
        }
    })

    const form = document.querySelector("#loginForm");

    form.addEventListener("submit", (e) => {
        const fieldValue = document.querySelector("#username").value;
        if (fieldValue == null || fieldValue == "") {
            //field was empty, prevent submit
            e.preventDefault();
            console.log("you must enter a username");
        }
    })
})




window.addEventListener('DOMContentLoaded', (event) => {
    let divs = document.querySelectorAll("div")

    for (const div of divs) {
        div.setAttribute("style", "backgroundcolor=red")
    }
})



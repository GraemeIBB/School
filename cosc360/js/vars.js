window.addEventListener('DOMContentLoaded', (event) => {
    let div = document.getElementById("container")
    let style = document.getElementById("styles")
    div.innerHTML = "<input type=\"text\" id=\"queryInput\"></input>\n<input type=\"submit\" id=\"submitBtn\"></input>\n"

    // Get the input and button elements
    let queryInput = document.getElementById("queryInput")
    let submitBtn = document.getElementById("submitBtn")
    let userQuery;

    // Add click event to submit button
    submitBtn.addEventListener('click', () => {
        userQuery = queryInput.value
        console.log("User typed:", userQuery)

        // Use the query in your code here
        // For example:
        // processQuery(userQuery)
    })

    // Optional: Also trigger on Enter key press
    queryInput.addEventListener('keypress', (e) => {
        userQuery = queryInput.value
        style.innerHTML = userQuery
        //if (e.key === 'Enter') {
        //    let userQuery = queryInput.value
        //    console.log("User typed:", userQuery)
        //}
    })
})



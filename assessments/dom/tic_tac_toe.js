let board = document.getElementById("gameBoard")
const reset = document.getElementById("reset")
const cells = Array.from(document.getElementsByClassName("cell"))
let store = ""

reset.addEventListener("click", () => {
    cells.forEach(cell => {
        cell.innerHTML = ""
    })

    store = ""
})

board.addEventListener("click", (e) => {
    if (e.target.innerHTML === ""){
        if (store === "O" || store === "") {
            e.target.innerHTML = "X"
            store = "X"
        } else {
            e.target.innerHTML = "O"
            store = "O"
        }
    }
})


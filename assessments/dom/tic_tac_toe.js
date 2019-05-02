let board = document.getElementById("gameBoard")
const reset = document.getElementById("reset")
const cells = Array.from(document.getElementsByClassName("cell"))
let store = ""

reset.addEventListener("click", () => {
    clearSquares()
    store = ""
})

board.addEventListener("click", (e) => {
    fillSquare(e)
})

function clearSquares() {
    cells.forEach(cell => {
        cell.innerHTML = ""
    })
}

function fillSquare(event) {
    if (event.target.innerHTML === ""){
        if (store === "O" || store === "") {
            event.target.innerHTML = "X"
            store = "X"
        } else {
            event.target.innerHTML = "O"
            store = "O"
        }
    }
}
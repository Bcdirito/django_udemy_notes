let playerBlue = {
    color: "Blue"
}

let playerRed = {
    color: "Red"
}

playerBlue["name"] = prompt("Player One: Enter Your Name, you will be Blue")
playerRed["name"] = prompt("Player Two: Enter Your Name, you will be Red")

const buttons = $(".button")
const directions = $(".directions")
let currentPlayer;
let currentColor;

const gray = "rgb(128, 128, 128)"
const blue = "rgb(0, 0, 255)"
const red = "rgb(255, 0, 0)"

$(window).on("load", function() {
    if (!playerBlue["name"]){
        playerBlue["name"] = null
    }

    if (!playerRed["name"]){
        playerRed["name"] = null
    }

    currentPlayer = playerBlue
    currentColor = blue
    changeDirections(currentPlayer)
})

buttons.on("click", function() {
    let column = $(`.${$(this)[0].className.split(" ")[1]}`)
    changeColor(column)
})

function changePlayer() {
    console.log("made it here")
    if (currentColor === blue) {
        currentPlayer = playerRed
        currentColor = red
    } 
    else if(currentColor === red) {
        currentPlayer = playerBlue
        currentColor = blue
    }
    changeDirections(currentPlayer)
}

function changeDirections(player){
    directions.eq(0).text(`${player["name"]}: it is your turn, please pick a column to drop your ${player["color"]} chip.`)
}

function changeColor(column){
    for (let i = column.length - 1; i >= 0; i--){
        let cell = column.eq(i)
        if (cell.css("background-color") === gray){
            cell.css("background-color", currentColor)
            let row = $(`.${cell.attr("class").split(" ")[2]}`)
            winChecker(currentColor, column, row)
            break
        } else if (i === 0){
            alert("Please pick a different Column")
            break
        } else {
            continue
        }
    }
}

function winChecker(color, column, row){
    columnChecker(color, column)
    rowChecker(color, row)

    if ($("body").css("background-color") === "rgb(255, 255, 255)") changePlayer()
}

function columnChecker(currentColor, currentColumn){
    let store = 1
    for (let i = currentColumn.length - 1; i >= 1; i--){
        if (currentColumn.eq(i).css("background-color") === currentColor && currentColumn.eq(i - 1).css("background-color") === currentColor){
            store += 1
        } else {
            break
        }

        if (store === 4){
            win()
            break
        }
    }
}

function rowChecker(currentColor, currentRow){
    let store = 1
    for (let i = 1; i <= currentRow.length; i++){
        if (currentRow.eq(i).css("background-color") === currentColor && currentRow.eq(i + 1).css("background-color") === currentColor){
            store += 1
        } else {
            break
        }

        if (store === 4){
            win()
            break
        }
    }
}

function win(){
    directions.eq(0).text(`${currentPlayer["name"]} has won! Refresh your browser to play again!`)
    $("body").css("background-color", currentColor)
    $(".board").html("")
}


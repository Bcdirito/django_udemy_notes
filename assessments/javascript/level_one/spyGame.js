const firstName = prompt("What is your first name?")
const lastName = prompt("What is your last name?")
const age = Number(prompt("How old are you?"))
const height = prompt("How tall are you in centimeters? (Height in inches * 2.54)")
const pet = prompt("What is the name of your pet?(Enter \"none\" if you don't have a pet)")

if (firstName[0].toLowerCase() === lastName[0].toLowerCase()){
    if (age > 20 && age < 30){
        if (height >= 170){
            if (pet[pet.length - 1] === "y"){
                alert("Find the secret message")
                console.log("I see u spyin'")
            }
        }
    }
}
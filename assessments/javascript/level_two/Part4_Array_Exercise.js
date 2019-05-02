// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
let roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

function addStudent(){
    student = prompt("Please enter their name")
    roster.push(student)
}


// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

function removeStudent(){
    let name = prompt("Which student would you like to remove?")
    roster = roster.filter(student => {
        return student.toLowerCase() !== name.toLowerCase()
    })
}

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.

function displayStudents() {
    if (roster.length > 0){
        roster.forEach(student => {
            console.log(student)
        })

        alert("Please check the console for to view the students")

    } else alert("No students enrolled! Please add to the roster.")
}

// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
let start = prompt("Would you like to start the roster web app? (y/n)")

if (start === "y"){
    let command = prompt("Would you like to add, remove, display, or quit?").toLowerCase()
    while (command !== "quit"){
        if (command === "add") addStudent()
        else if (command === "remove") removeStudent()
        else if (command === "display") displayStudents()

        command = prompt("Would you like to add, remove, display, or quit?").toLowerCase()
    }
}
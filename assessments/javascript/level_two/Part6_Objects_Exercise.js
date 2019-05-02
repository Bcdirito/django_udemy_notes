// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function() {
    let total = 0
    this.name.split("").forEach(s => {
      if (s.match(/[a-zA-Z]/g)) total += 1
    })

    return total
  }
}

// Add a method called nameLength that prints out the
// length of the employees name to the console.


///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}

// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:

// Name is John Smith, Job is Programmer, Age is 31.
function employeeAlert(employee){
  let finalArr = []
  for (const key in employee){
    let capitalKey = key[0].toUpperCase() + key.split("").slice(1).join("")
    finalArr.push(`${capitalKey} is ${employee[key]}`)
  }

  return finalArr.join(", ") + "."
}


///////////////////
// PROBLEM 3 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function() {
    let nameArr = this.name.split(" ")
    return nameArr[nameArr.length-1]
  }
}

// Add a method called lastName that prints
// out the employee's last name to the console.

// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp

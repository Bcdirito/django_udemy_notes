// jQuery Notes

// Can be installed with CDN like Bootstrap

// To select all of something use $("")
// Example grabbing all a tags, all container class elements, and all special id elements
const anchors = $("a")
const containers = $(".container")
const specials = $(".special")

// To edit css
anchors.css(newCSS)

let newCSS = {
    // properties
}

// or

anchors.eq(0).css("color", "orange")

// Editing Text
$("h1").text("TEXT")

// Editing HTML
$("h1").html("<em>TEXT</em>")

// Attributes
$("what you want to change").eq(idx).attr("attribute", "what you're changing it to")

// Values
$("what you want to change").eq(idx).val("new value")

// Classes
// Adding a class
$("what you're grabbing").addClass("name of class")

// Removing a class
$("what you're grabbing").removeClass("name of class")

// Toggling Class
$("what you're grabbing").toggleClass("name of class")

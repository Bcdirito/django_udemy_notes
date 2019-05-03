// jQuery Events Notes

// Click Event Examples
$("h1").click(function(){
    console.log("There was a click!")
})

$("li").click(function(){
    console.log("any li was clicked!")
})

// Editing what's rendered
$("h1").click(function(){
    $(this).text("I was changed!")
})

// Key Press Event Examples
$("input").eq(0).keypress(function(){
    $("h3").toggleClass("turnBlue")
})

$("input").eq(0).keypress(function(){
    console.log(event)
})

$("input").eq(0).keypress(function(){
    if (event.which === 13){
        $("h3").toggleClass("turnBlue")
    }
})


// On Method
// Acts like addEventListener()
// Examples

$("h1").on("dbclick"), function(){
    $(this).toggleClass("turnBlue")
}

$("h1").on("mouseenter"), function(){
    $(this).toggleClass("turnBlue")
}

// Effects and Animations Examples
$("input").eq(1).on("click", function() {
    $(".container").fadeOut(3000)
})

$("input").eq(1).on("click", function() {
    $(".container").slideUp(3000)
})




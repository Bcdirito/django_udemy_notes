# Decorates Notes

# Functions that modify functionality of another function
# Often used in Django

# locals() -> To grab all local variables as a dictionary
# globals() -> To grab all global variables as a dictionary

# Example of variable value being return of function
def hello(name="Brian"):
    return "hello {input_name}".format(input_name = name)
    
new_hello = hello

print(new_hello())

# Nesting Functions Example
def second_example_hello(name="Brian"):
    print("This is in the second example")

    def greet():
        return "This string is inside greet()"
    
    def welcome():
        return "This string is inside welcome()"
    
    print(greet())
    print(welcome())
    print("End of hello()")

second_example_hello()

# Another Example
def third_example_hello(name="Brian"):
    print("This is in the third example")

    def greet():
        return "This string is inside greet()"
    
    def welcome():
        return "This string is inside welcome()"
    
    if name == "Brian":
        return greet
    else:
        return welcome

# If you are inputting an argument, put it here
x = third_example_hello("Ryan")

print(x())

# Passing Function as Argument
def fourth_example_hello():
    return "Hi Brian!"

def other(func):
    print("Hello")
    print(func())

other(fourth_example_hello)

# Decorater Example:

def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func

# @new_decorator serves as saving func_needs_decorator variable
@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")

# Longer Syntax
# func_needs_decorator =  new_decorator(func_needs_decorator)

# func_needs_decorator()

# Shorter Syntax utilizing @ symbol
func_needs_decorator()
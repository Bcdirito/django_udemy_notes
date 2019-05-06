# Scope Notes

# LEGB Rule of Scope Order:

# Local
# Enclosing Function locals
# Global
# Buil-In

# Examples
x = 25

def my_func():
    x = 50
    return x

print(x) 
print(my_func())

# Line 17 prints 25
# Line 18 print 50

# Be careful not to overwrite built in function names by assigning variables with that name

# To make changes to global variable, call global /variable_name/ inside of a function


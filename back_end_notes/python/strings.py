# String Notes

# To get quotes in a string, use the other set of quotes
# Example

string = "I'm a 'dog'"

# Slicing
# 3 Parts (Beginning, End, Steps)
# The end index is not inclusive
# Example:
string[::2]

# strings indices are immutable

# Print Formatting
# String Interpolation
# Example
x = "Insert another string here: {}".format("INSERT ME!")
y = "Item One: {x} Item Two: {x}".format(x )
print(x)
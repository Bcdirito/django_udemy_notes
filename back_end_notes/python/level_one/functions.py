# Function Notes

# To get docstring, input """
# Example

def my_func(param1="default"):
    """
    THIS IS THE DOCSTRING
    """
    print("my first python function! {}".format(param1))

my_func()

# to check type, use type()
# simplest method for error catching with data types

# Lambda Expression
# Example:

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

evens = filter(lambda num:num%2 == 0, my_list)

print(evens)
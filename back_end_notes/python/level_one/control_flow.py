# Control Flow Notes

# Iterate through dictionaries is same as for loop
# Keys do not print out in order

# Iterating through tuples
# Example with tuple unpacking

my_pairs = [(1,2), (3,4), (5,6)]

for (tup1, tup2) in my_pairs:
    print(tup1)
    print(tup2)


# range
# Example gets you all even numbers 0-20
print(list(range(0, 21, 2)))

# range() is great for memory usage

# List Comprehension
# Example

x = [1, 2, 3, 4]

out = [num**2 for num in x]
print(out)
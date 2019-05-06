# List Notes

# Unlike a string, list elements are mutable

# .extend() is how you would concat lists
# .pop() can be given any index
# .reverse() and .sort() both mutate the list

# Nested Lists
# Example

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix[0][0] = 1

first_col = [row[0] for row in matrix]
print(first_col)
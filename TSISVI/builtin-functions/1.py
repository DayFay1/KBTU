from functools import reduce

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the reduce() function to multiply all the numbers in the list
result = reduce(lambda x, y: x * y, numbers)

# Print the result
print(result)
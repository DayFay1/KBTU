import math
import time

# Prompt the user for a number and a duration in milliseconds
number = int(input("Enter a number: "))
milliseconds = int(input("Enter a duration in milliseconds: "))

# Pause the program for the specified duration
time.sleep(milliseconds / 1000)

# Compute the square root of the number
result = math.sqrt(number)

# Print the result
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
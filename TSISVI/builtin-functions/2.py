# Define a string
string = input()

# Initialize counters for upper case letters and lower case letters
upper_count = 0
lower_count = 0

# Loop through each character in the string
for char in string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

# Print the results
print("Number of upper case letters:", upper_count)
print("Number of lower case letters:", lower_count)

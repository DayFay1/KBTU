# Open the file for reading
with open("test.txt", "r") as file:

    # Initialize a variable to count the number of lines
    count = 0

    # Loop through each line in the file
    for line in file:
        # Increment the count for each line
        count += 1

# Print the total number of lines in the file
print("Total number of lines:", count)
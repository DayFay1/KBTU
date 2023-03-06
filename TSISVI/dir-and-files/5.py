# List of items to write to the file
my_list = ["apple", "banana", "cherry", "date"]

# Open the file for writing
with open("testW.txt", "w") as file:

    # Loop through each item in the list and write it to the file
    for item in my_list:
        file.write(item + "\n")

# Print a message indicating that the file was written
print("List written to file.")
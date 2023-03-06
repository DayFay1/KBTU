# Open the source file for reading
with open("source_file.txt", "r") as source_file:

    # Open the destination file for writing
    with open("destination_file.txt", "w") as destination_file:

        # Loop through each line in the source file
        for line in source_file:

            # Write the line to the destination file
            destination_file.write(line)

# Print a message indicating that the file has been copied
print("File copied.")

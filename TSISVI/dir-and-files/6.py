import os
import string

# Directory to create files in
directory = "E:\Программы\GIt_P\KBTU\TSISVI\Alphabet"

# Loop through the letters of the alphabet
for letter in string.ascii_uppercase:

    # Create a filename for the current letter in the specified directory
    filename = os.path.join(directory, letter + ".txt")

    # Create a new file with the filename
    with open(filename, "w") as file:
        # Write some text to the file
        file.write("This is the file for letter " + letter + ".")


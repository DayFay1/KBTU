import os

# Specified path
path = "E:\Программы\GIt_P\KBTU"

# Check if path exists
if os.path.exists(path):
    print("Path exists.")

    # Check if path is readable
    if os.access(path, os.R_OK):
        print("Path is readable.")
    else:
        print("Path is not readable.")

    # Check if path is writable
    if os.access(path, os.W_OK):
        print("Path is writable.")
    else:
        print("Path is not writable.")

    # Check if path is executable
    if os.access(path, os.X_OK):
        print("Path is executable.")
    else:
        print("Path is not executable.")
else:
    print("Path does not exist.")
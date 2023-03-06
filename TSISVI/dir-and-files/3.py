import os

# Specified path
path = "E:\Программы\GIt_P\KBTU"

# Check if path exists
if os.path.exists(path):
    print("Path exists.")

    # Get filename and directory portion of the given path
    filename = os.path.basename(path)
    directory = os.path.dirname(path)

    # Print filename and directory portion
    print("Filename:", filename)
    print("Directory:", directory)

else:
    print("Path does not exist.")
import os

# Specified path
path = "E:\Программы\GIt_P\KBTU"

# Get list of directories present in the specified path
dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

# Get list of files present in the specified path
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# Print the list of directories and files
print("List of Directories:")
for d in dirs:
    print(d)

print("\nList of Files:")
for f in files:
    print(f)
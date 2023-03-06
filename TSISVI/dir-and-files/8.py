import os

# Specify the path of the file to be deleted
path = "E:\Программы\GIt_P\KBTU\TSISVI\dir-and-files\deleteDestiny.cpp"

# Check if the file exists
if os.path.exists(path):
    
    # Check if the file is accessible
    if os.access(path, os.W_OK):
        
        # Delete the file
        os.remove(path)
        print("File deleted.")
        
    else:
        print("You do not have write access to the file.")
        
else:
    print("The file does not exist.")

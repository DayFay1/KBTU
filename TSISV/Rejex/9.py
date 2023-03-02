import re

# Read in the contents of the file "row.txt" as a string
with open("row.txt", "r", encoding="UTF-8") as f:
    contents = f.read()

# Insert spaces between words starting with capital letters
new_contents = re.sub(r"([a-z])([A-Z])", r"\1 \2", contents)
print(new_contents)

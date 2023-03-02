import re

# Read in the contents of the file "row.txt" as a string
with open("row.txt", "r", encoding="UTF-8") as f:
    contents = f.read()

# Define the regular expression pattern
pattern = r"^a.*b$"
regex = re.compile(pattern)

# Iterate over the lines in the contents and check if they match the pattern
# match = regex.findall(contents)
for line in contents.splitlines():
    match = re.search(pattern, line)
    if match is not None:
            print(f'{line}: Match')
            continue
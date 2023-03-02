import re

# Read in the contents of the file "row.txt" as a string
with open("row.txt", "r", encoding="UTF-8") as f:
    contents = f.read()

# Split each line of the file at uppercase letters
lines = contents.split('\n')
for line in lines:
    split_line = re.findall('[A-Z][^A-Z]*', line)
    print(split_line)
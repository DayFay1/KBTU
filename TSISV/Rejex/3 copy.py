import re

# Read in the contents of the file "row.txt" as a string
with open("row.txt", "r", encoding="UTF-8") as f:
    contents = f.read()

# Define the regular expression pattern
pattern = r'[a-z]+_[a-z]+'

# Find all matches in the contents
matches = re.findall(pattern, contents)

# Print the matches
print(matches)



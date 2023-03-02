import re

# Read in the contents of the file "row.txt" as a string
with open("row.txt", "r", encoding="UTF-8") as f:
    contents = f.read()

# Define the regular expression pattern
pattern = r'.*a.*?(b.*?){2,3}.*$'
regex = re.compile(pattern)

# Iterate over the lines in the contents and check if they match the pattern
# match = regex.findall(contents)
for line in contents.splitlines():
    match = re.search(pattern, line)
    if match is not None:
        b_count = match.group(0).count('b')
        if b_count >= 2 and b_count <= 3:
            print(f'{line}: Match')
            continue


import re

# Read in the contents of the file "row.txt" as a string
with open("row.txt", "r", encoding="utf-8") as f:
    contents = f.read()

# Match string with 'a' followed by two or three 'b's, with some characters allowed after the last 'b'
regex = re.compile(r'a.*?(b.*?){2,3}.*$')
match = regex.findall(contents)
print(match)
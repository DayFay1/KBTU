import re

# Read in the contents of the file "row.txt" as a string
with open("row.txt", "r",encoding= 'UTF-8') as f:
    contents = f.read()

# Exercise 1: Match string with 'a' followed by zero or more 'b's
regex1 = re.compile(r".*a.*b*")
match1 = regex1.findall(contents)
print(match1)
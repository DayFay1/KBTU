import re

# Read in the contents of the file "row.txt" as a string
with open("row.txt", "r",encoding= 'UTF-8') as f:
    contents = f.read()
# Exercise 5: Match string with 'a' followed by anything, ending in 'b'
regex5 = re.compile(r"^a.*b$")
match5 = regex5.findall(contents)
print(match5)
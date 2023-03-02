import re

# Read in the contents of the file "row.txt" as a string
with open("row.txt", "r",encoding= 'UTF-8') as f:
    contents = f.read()

# Exercise 1: Match string with 'a' followed by zero or more 'b's
print('Exercise 1: Match string with ' + 'a' +' followed by zero or more ' + 'b')
regex1 = re.compile(r"ab*")
match1 = regex1.findall(contents)
print(match1)

# Exercise 2: Match string with 'a' followed by 2-3 'b's
print('Exercise 2: Match string with ' + 'a' +' followed by 2-3 ' + 'b' + 's')
regex2 = re.compile(r"ab{2,3}")
match2 = regex2.findall(contents)
print(match2)

# Exercise 3: Find sequences of lowercase letters joined with underscore
print('Exercise 3: Find sequences of lowercase letters joined with underscore')
regex3 = re.compile(r"[a-z]+_[a-z]+")
match3 = regex3.findall(contents)
print(match3)

# Exercise 4: Find sequences of one upper case letter followed by lower case letters
print('Exercise 4: Find sequences of one upper case letter followed by lower case letters')
regex4 = re.compile(r"[A-Z][a-z]+")
match4 = regex4.findall(contents)
print(match4)

# Exercise 5: Match string with 'a' followed by anything, ending in 'b'
print('Exercise 5: Match string with ' + 'a' +' followed by anything, ending in ' + 'b' + '')
regex5 = re.compile(r"a.*b")
match5 = regex5.findall(contents)
print(match5)

# Exercise 6: Replace all occurrences of space, comma, or dot with colon
print('Exercise 6: Replace all occurrences of space, comma, or dot with colon')
regex6 = re.compile(r"[ ,.]+")
replace6 = ":"
new_string6 = regex6.sub(replace6, contents)
print(new_string6)

# Exercise 7: Convert snake case string to camel case string
print('Exercise 7: Convert snake case string to camel case string')
regex7 = re.compile(r"_([a-z])")
replace7 = lambda match: match.group(1).upper()
new_string7 = regex7.sub(replace7, contents)
print(new_string7)

# Exercise 8: Split string at uppercase letters
print('Exercise 8: Split string at uppercase letters')
regex8 = re.compile(r"[A-Z][^A-Z]*")
match8 = regex8.findall(contents)
print(match8)

# Exercise 9: Insert spaces between words starting with capital letters
print(' Exercise 9: Insert spaces between words starting with capital letters')
regex9 = re.compile(r"([A-Z][a-z]+)")
replace9 = r" \1"
new_string9 = regex9.sub(replace9, contents)
print(new_string9)

# Exercise 10: Convert camel case string to snake case string
print('Exercise 10: Convert camel case string to snake case string')
regex10 = re.compile(r"(?<!^)([A-Z])")
replace10 = lambda match: "_" + match.group(1).lower()
new_string10 = regex10.sub(replace10, contents)
print(new_string10)

import re

with open('row.txt', 'r') as f:
    string = f.read()

pattern = r'ab*'
matches = re.findall(pattern, string)
print(matches)
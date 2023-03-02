import re

# Read in the contents of the file "row.txt" as a string
with open("row.txt", "r",encoding= 'UTF-8') as f:
    contents = f.read()
# 3. Finds sequences of lowercase letters joined with an underscore.
pattern_3 = r'[a-z]+_[a-z]+'
result_3 = re.findall(pattern_3, contents)
print(result_3)

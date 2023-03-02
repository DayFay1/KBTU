import re

# Open the file for reading and reading the contents
with open('row.txt', 'r', encoding='UTF-8') as file:
    contents = file.read()

# Define the regular expression pattern
pattern = r'[ ,.]'

# Replace all occurrences of the pattern with a colon
replaced_text = re.sub(pattern, ':', contents)

# Open the file for writing and write the replaced text
with open('row_copy.txt', 'w', encoding='UTF-8') as file:
    file.write(replaced_text)

# Print a message indicating the replacement is done
print('Replacement completed.')
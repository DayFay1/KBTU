import re

# Read the contents of the file
with open("camel.txt", "r", encoding="utf-8") as f:
    contents = f.read()

# Define a function to convert camel case to snake case
def camel_to_snake(camel_case_str):
    # Convert the first character to lowercase
    snake_case_str = camel_case_str[0].lower()

    # Convert the rest of the characters
    snake_case_str += re.sub(r'([A-Z])', r'_\1', camel_case_str[1:]).lower()

    return snake_case_str

# Find all camel case strings in the file and replace them with snake case
snake_case_contents = re.sub(r'([a-z]+[A-Z]+[a-zA-Z]*)', lambda x: camel_to_snake(x.group(0)), contents)

# Write the new contents to the output file
with open("snake.txt", "w", encoding="utf-8") as f:
    f.write(snake_case_contents)
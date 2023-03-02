def snake_to_camel_case(snake_str):
    components = snake_str.split('_')
    # Capitalize the first letter of each component except the first one
    camel_case = ''.join(x.capitalize() if i else x for i, x in enumerate(components))
    return camel_case

# Read in the input string from the file "row.txt"
with open('snake.txt', 'r', encoding='utf-8') as f:
    snake_case_str = f.read().strip()

# Convert the input string to camel case
camel_case_str = snake_to_camel_case(snake_case_str)

# Write the camel case string to a new file "camel.txt"
with open('camel.txt', 'w', encoding='utf-8') as f:
    f.write(camel_case_str)

print('Successfully wrote camel case string to "camel.txt"')
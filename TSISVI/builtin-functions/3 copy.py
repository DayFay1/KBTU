# Define a function to check if a string is palindrome or not
def is_palindrome(string):
    # Convert the string to lowercase
    string = string.lower()
    # Remove all whitespace from the string
    string = string.replace(" ", "")
    # Reverse the string
    reversed_string = string[::-1]
    # Check if the original string is equal to the reversed string
    if string == reversed_string:
        return True
    else:
        return False

# Prompt the user for a string
string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

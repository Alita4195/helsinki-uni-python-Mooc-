# Write your solution here
# the password should always contain at least one lowercase alphabet
# the generated password should also contain one or more numbers
# the generated password should also contain one or more of these special characters: !?=+-()#.
# You may assume the function will only be called with combinations of arguments

import random
import string

def generate_strong_password(length: int, include_numbers: bool, include_special_chars: bool):
    password = ""

    # Ensure at least one lowercase alphabet
    password += random.choice(string.ascii_lowercase)

    # Adjust length based on additional requirements
    length -= 1

    # Generate the remaining characters
    chars = string.ascii_lowercase
    if include_numbers:
        chars += string.digits
        password += random.choice(string.digits)
        length -= 1
    if include_special_chars:
        chars += "!?=+-()#"
        password += random.choice("!?=+-()#")
        length -= 1

    for i in range(length):
        password += random.choice(chars)

    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(2, False, False))






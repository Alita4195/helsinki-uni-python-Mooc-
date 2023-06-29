# Write your solution here
import random
import string

def generate_password(length:int):
    password=""
    for i in range(length):
        password += random.choice(string.ascii_lowercase)
    return password

if __name__ == "__main__":
    length = 8
    generated_password = generate_password(length)
    print(generated_password)


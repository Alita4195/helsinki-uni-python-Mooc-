# Write your solution here
import string

def separate_characters(my_string):
    lowercase_uppercase = ""
    punctuation = ""
    others = ""

    for char in my_string:
        if char in string.ascii_letters:
            lowercase_uppercase += char
        elif char in string.punctuation:
            punctuation += char
        else:
            others += char

    return (lowercase_uppercase, punctuation, others)

if __name__ == "__main__":
# Example usage
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])  # Output: OléHeyareümläütswörking
    print(parts[1])  # Output: !!!,,
    print(parts[2])  # Output:   ? Hey are ümläüts wörking
    separate_characters(parts)
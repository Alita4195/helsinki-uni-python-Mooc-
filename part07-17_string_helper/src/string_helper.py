# Write your solution here
def change_case(orig_string: str):
    new_1string = orig_string.swapcase()
    return new_1string

def split_in_half(orig_string: str):

    string_length = len(orig_string)

    if string_length % 2 == 0:
        half_string = orig_string[0:int(string_length/2)]
        another_half_string = orig_string[int(string_length/2):]
    else:
        half_string = orig_string[0:int(string_length/2)]
        another_half_string = orig_string[int(string_length/2):]

    return half_string, another_half_string

def remove_special_characters(orig_string: str):
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    new_string = ""

    for char in orig_string:
        if char in allowed_chars:
            new_string += char

    return new_string


if __name__ == "__main__":
    orig_string = "I want an apple!"
    result1 = change_case(orig_string)
    print(result1)
    result2 = split_in_half(orig_string)
    print(result2)
    result3 = remove_special_characters(orig_string)
    print(result3)




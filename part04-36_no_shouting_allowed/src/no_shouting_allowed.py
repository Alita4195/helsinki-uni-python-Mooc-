# Write your solution here
def no_shouting(strings:list):
    new_strings=[]
    for item in strings:
        if not item.isupper():
            new_strings.append(item)
    return(new_strings)
if __name__ == "__main__":
    no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower"])
    no_shouting(["Abc"])
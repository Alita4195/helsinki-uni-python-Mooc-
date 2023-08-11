# Write your solution here
def most_common_character(str):
    most_common = max(set(str), key=str.count)
    return most_common
if __name__ == "__main__":
    most_common_character("abcdbde")


    
    
    
    


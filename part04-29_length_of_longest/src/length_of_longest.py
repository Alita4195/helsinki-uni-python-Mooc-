# Write your solution here
def length_of_longest(my_list:str):
    best=0
    for item in my_list:
        if len(item) > best:
            best=len(item)
    return best
if __name__=='__main__':
    length_of_longest(["first", "second", "fourth", "eleventh"])
        
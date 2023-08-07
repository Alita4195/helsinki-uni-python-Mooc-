# Write your solution here
def list_of_stars(my_list:list):
    index=0
    while index < len(my_list):
        print("*"*my_list[index])
        index += 1

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])
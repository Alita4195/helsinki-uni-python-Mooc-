# Write your solution here
# You can test your function by calling it within the following block
def range_of_list(my_list: list):
    range=max(my_list)-min(my_list)
    return range
    

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
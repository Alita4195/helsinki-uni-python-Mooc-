# Write your solution here
def distinct_numbers(my_list: list):
    distinct_numbers=[]
    my_list.sort()
    for item in my_list:
        if item in distinct_numbers:
            continue
        else:
            distinct_numbers.append(item)
    return distinct_numbers
if __name__=='__main__':
    distinct_numbers([3, 2, 2, 1, 3, 3, 1])

            
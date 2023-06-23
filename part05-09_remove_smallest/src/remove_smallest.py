# Write your solution here
def remove_smallest(numbers: list):
    smallest_dig=numbers[0]
    for i in range(len(numbers)):
        if numbers[i]<smallest_dig:
            smallest_dig=numbers[i]
    new_list=numbers.remove(smallest_dig)
    return (new_list)
if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    
            


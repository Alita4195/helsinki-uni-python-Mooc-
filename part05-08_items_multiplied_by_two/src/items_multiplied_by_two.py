# Write your solution here
def double_items(numbers: list):
    numbers_doubled=[]
    for item in numbers:
        new_item=item*2
        numbers_doubled.append(new_item)
    return numbers_doubled
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)


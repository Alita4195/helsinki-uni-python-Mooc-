# Write your solution here
def even_numbers(my_list:list):
    even_numbers = []
    for item in my_list:
        if item % 2==0:     
            even_numbers.append(item)
    print (even_numbers) 
if __name__ == "__main__":
    even_numbers([1, 2])
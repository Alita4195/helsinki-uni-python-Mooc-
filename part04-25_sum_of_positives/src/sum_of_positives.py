# Write your solution here
def sum_of_positives(my_list: list):
    sum_of_positives=0
    for n in my_list:
        if n>0:
            sum_of_positives+=n       
    return sum_of_positives
if __name__ == "__main__":
    sum_of_positives([1, 2])

   
    


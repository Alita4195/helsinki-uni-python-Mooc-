# Write your solution here
# from random import sample


# def lottery_numbers(amount: int, lower: int, upper: int):

#     number_pool = list(range(lower, upper))
#     lottery_numbers = sample(number_pool, amount)
#     sorted_numbers = sorted(lottery_numbers)
    
#     for item in sorted_numbers:
#         return(item)  

#     #print(lottery_numbers)# generate a list of random numbers
# if __name__ == "__main__":
#     lottery_numbers(1, 1, 10)

# # for number in lottery_numbers(7, 1, 40):
# #     print(number)

from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper))
    lottery_numbers = sample(number_pool, amount)
    sorted_numbers = sorted(lottery_numbers)
    return (sorted_numbers)


if __name__ == "__main__":
    lottery_numbers(1, 1, 10)


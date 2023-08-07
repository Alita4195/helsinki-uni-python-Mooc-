# Write your solution here
from fractions import Fraction

def fractionate(amount):
    fraction = Fraction(1, amount)
    fractions_list = [fraction] * amount
    return fractions_list

# Example usage
if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))


    

    
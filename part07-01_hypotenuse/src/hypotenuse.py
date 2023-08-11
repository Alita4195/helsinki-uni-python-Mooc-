# Write your solution here
#Symbolic statement: 
def hypotenuse(leg1: float, leg2: float):
    from math import sqrt
    a=leg1*leg1
    b=leg2*leg2
    c=a+b
    return sqrt(c)
    
if __name__ == "__main__":
    hypotenuse(3,4)
    

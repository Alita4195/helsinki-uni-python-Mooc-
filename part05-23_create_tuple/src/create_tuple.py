# Write your solution here
def create_tuple(x: int, y: int, z: int):
    if x<y and x<z:
        smallest_dig=x
    elif y<x and y<z:
        smallest_dig=y
    else:
        smallest_dig=z
    if x>y and x>z:
        greatest_dig=x
    elif y>x and y>z:
        greatest_dig=y
    else:
        greatest_dig=z
    sum=x+y+z
    return(smallest_dig, greatest_dig, sum)
if __name__ == "__main__":
    create_tuple(5, 3, -1)

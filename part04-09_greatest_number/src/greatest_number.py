# Write your solution here
# You can test your function by calling it within the following block
def greatest_number(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    if c>b and c>a:
        return c
    if a==b==c:
        return a
    if a<b and b==c:
        return b
    if a>b and a==c:
        return a
    if a==b and a>c:
        return a
if __name__ == "__main__":
    greatest = greatest_number(1,1,-100)
    print(greatest)
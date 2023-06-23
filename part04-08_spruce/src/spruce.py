# Write your solution here
# You can test your function by calling it within the following block
def spruce(a):
    print("a spruce!")
    sign="*"
    row=a
    while 0<row<=a:
        print(" " * (row-1) + sign)
        sign+="**"
        row-=1
    print(" " * (a-1) + "*")
    
if __name__ == "__main__":
    spruce(3)
    

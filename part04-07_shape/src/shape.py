# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
#The first parameter also specifies the width of a rectangle矩形, while the third parameter specifies its height.
#The fourth parameter specifies the filler character of the rectangle.
def line(width_1,a):
    print(width_1*a)
def shape(width_1,a,tall,b):
    width=0
    while width<width_1:
        width+=1
        line(width,a)
    while tall>0:
        tall-=1
        line(width_1,b)
if __name__ == "__main__":
    shape(5, "x", 2, "o")
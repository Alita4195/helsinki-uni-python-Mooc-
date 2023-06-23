# Copy here code of line function from previous exercise
def line(a,b):
    print(a*b)
def triangle(size):
    rows=0
    # You should call function line here with proper parameters
    while rows<=size:
        line(rows, "#")
        rows+=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

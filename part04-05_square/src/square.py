# Copy here code of line function from previous exercise
def line(a,b):
    print(a*b)
def square(size, character):
    rows=size
    # You should call function line here with proper parameters
    while rows>0:
        line(size, character)
        rows-=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "+")
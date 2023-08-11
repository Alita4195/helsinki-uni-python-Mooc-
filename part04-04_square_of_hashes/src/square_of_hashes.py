def line(a,b):
    print(a*b)
def square_of_hashes(size):
    rows=size
    while rows>0:
        line(size,"#")
        rows-=1
if __name__ == "__main__":
    square_of_hashes(5)

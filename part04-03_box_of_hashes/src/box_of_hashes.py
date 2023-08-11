# Copy here code of line function from previous exercise
def hashes(a):
    print("#"*a)
def box_of_hashes(height):
    while height>0:
        hashes(10)
        height-=1
if __name__=="__main__":
    box_of_hashes(5)
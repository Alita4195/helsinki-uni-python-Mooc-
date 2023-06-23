def read_matrix():
    with open("matrix.txt") as file:
        m = []
        for row in file:
            mrow = []
            items = row.split(",")
            for item in items:
                mrow.append(int(item))
            m.append(mrow)
 
    return m
 
# Combines the rows of a matrix into a single list
def combine(matriisi:list):
    mlist = []
    for row in matriisi:
        mlist += row
    
    return mlist

if __name__=="__main__":
    print(combine(read_matrix()))
def read_matrix():
    with open("matrix.txt") as file:
        m = []
        for row in file:
            mrow = []
            items = row.split(",")
            for item in items:
                mrow.append(int(item))
            m.append(mrow)
 
    return m
 
# Combines the rows of a matrix into a single list
def combine(matriisi:list):
    mlist = []
    for row in matriisi:
        mlist += row
    
    return mlist
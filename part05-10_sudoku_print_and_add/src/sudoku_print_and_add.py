def print_sudoku(sudoku: list):
block=[]
while index<=6:
    for i in range(index,index+3):
        for j in range(index,index+3):
            block.append(sudoku[i][j])
    index+=3
    print(block)
    
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no]=number

    for i in sudoku:
        for j in i:
            
            if j==0:
                print (" _", end="")
            else:
                print(" "+str(j), end="")
        print()          
if __name__ == "__main__":
    sudoku  = [[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print_sudoku(sudoku)
    print()
    print("Three numbers added:")
    add_number(sudoku, 0, 0, 2)


    




    
        
        
        

                
                
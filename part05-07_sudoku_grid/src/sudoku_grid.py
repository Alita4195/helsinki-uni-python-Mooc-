def sudoku_grid_correct(sudoku: list): 
    index=0
    while index<=6:
        check_numbers=[]
        for i in range(index,index+3):
            for j in range(index,index+3):
                if sudoku[i][j] in check_numbers and sudoku[i][j]!=0:
                    return False
                check_numbers.append(sudoku[i][j])
        index+=3
    for item in sudoku:
        check_row=[]
        for x in item:
            if x in check_row and x!=0:
                return False
            check_row.append(x)
            
    for e in range(9):
        check_columns=[]
        for f in sudoku:
            if f[e] in check_columns and f[e]!=0:
                return False
            check_columns.append(f[e])
    
    return True            
if __name__ == "__main__":
    sudoku=[[6, 4, 9, 2, 8, 3, 1, 5, 7 ],[ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],[ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],[ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],[ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],[ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],[ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],[ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],[ 3, 0, 1, 5, 0, 6, 4, 9, 0 ]]
    sudoku_grid_correct(sudoku)
    
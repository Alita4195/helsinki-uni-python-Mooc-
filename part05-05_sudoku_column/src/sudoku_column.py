# Write your solution here
def column_correct(sudoku: list, column_no: int):
  numbers_check=[]
  for i in range(len(sudoku)):
    if sudoku[i][column_no] in numbers_check and sudoku[i][column_no]!=0:
        return False
    numbers_check.append(sudoku[i][column_no])
  return True

if __name__ == "__main__":
  sudoku = [[9, 0, 0, 0, 8, 0, 3, 0, 0],[2, 0, 0, 2, 5, 0, 7, 0, 0],[0, 2, 0, 3, 0, 0, 0, 0, 4],[2, 9, 4, 0, 0, 0, 0, 0, 0],[0, 0, 0, 7, 3, 0, 5, 6, 0],[7, 0, 5, 0, 6, 0, 4, 0, 0],[0, 0, 7, 8, 0, 3, 9, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 3],[3, 0, 0, 0, 0, 0, 0, 0, 2]]
  column_correct(sudoku, 0)
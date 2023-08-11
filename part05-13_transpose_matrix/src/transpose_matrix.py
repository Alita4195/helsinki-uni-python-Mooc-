# Write your solution here
def transpose(matrix: list):
    n = len(matrix)
    matrix[:] = [[row[i] for row in matrix] for i in range(n)]

if __name__ == "__main__":
    matrix = [[1, 2], [1, 2]]
    transpose(matrix)
    print (matrix)

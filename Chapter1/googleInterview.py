matrix = [[0]*m]*n
def set(i, j, newValue):
    matrix[i][j] = newValue
    return matrix

def subMatrix(i, j):
    row = len(matrix)
    col = len(matrix[0])
    sum = 0
    if i < 0 or j < 0 or i > row or j > col:
        return 0
    for row in range(i+1):
        for col in range(j+1):
            sum += matrix[row][col]
            
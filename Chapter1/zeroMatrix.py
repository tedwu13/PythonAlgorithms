#Write an algorithm such that if an element in an MxN matrix is 0, its entire row
#and column are set to 0.

def zeroProcess(matrix):
    row = len(matrix)    
    col = len(matrix[0])
    
    rowCount = []
    colCount = []
    for rowNum, row in enumerate(matrix):
        for cellCount, cell in enumerate(row):
            if cell == 0:
                rowCount.append(rowNum)
                colCount.append(cellCount)
    for row in rowCount:
        for c in range(0, col):
            matrix[row][c] = 0
    print matrix
    for col in colCount:
        for r in range(0, row):
            matrix[r][col] = 0
    print matrix
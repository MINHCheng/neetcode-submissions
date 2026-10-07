class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        topRow = False
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row == 0:
                        topRow = True
                    else:
                        matrix[row][0]=0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for row in range(1, len(matrix)):
                matrix[row][0] = 0
        if topRow:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        
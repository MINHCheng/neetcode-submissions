class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def traverse(row, col):
            print(matrix[row][col])
            if matrix[row][col] == target:
                return True
            if row + 1 < len(matrix) and matrix[row+1][0] <= target:
                return traverse(row+1, col)
            elif col + 1 < len(matrix[0]) and matrix[row][col+1] <= target:
                return traverse(row, col+1)
            return False
        return traverse(0,0)
        
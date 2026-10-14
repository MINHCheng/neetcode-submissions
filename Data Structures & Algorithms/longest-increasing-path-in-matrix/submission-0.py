class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        row, col = len(matrix), len(matrix[0])
        def dfs(r,c):
            if (r,c) in cache:
                return cache[(r,c)]
            direction = [(1,0), (-1,0), (0,1), (0,-1)]
            cache[(r,c)] = 1
            for d_r, d_c in direction:
                if not (r + d_r in range(row) 
                and c+d_c in range(col)
                and r + d_r >= 0 
                and c+d_c >= 0):
                    continue    
                if matrix[r+d_r][c+d_c] > matrix[r][c]:
                    cache[(r,c)] = max(1 + dfs(r+d_r,c+d_c), cache[(r,c)])
            return cache[(r,c)]
        res = 0
        
        for r in range(row):
            for c in range(col):
                dfs(r,c)
                res = max(res, cache[(r,c)])  
        return res       
        
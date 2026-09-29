class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        ret = []    
        pac, atl = set(), set()
        def dfs_pacific(r, c):
            pac.add((r,c))
            directions = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for row, col in directions:
                if (row not in range(ROWS) or col not in range(COLS)) or (row,col) in pac:
                    continue
                elif heights[row][col] >= heights[r][c]:
                    dfs_pacific(row, col)

        def dfs_atlantic(r,c):
            atl.add((r,c))
            directions = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for row, col in directions:
                if (row not in range(ROWS) or col not in range(COLS)) or (row,col) in atl:
                    continue
                elif heights[row][col] >= heights[r][c]:
                    dfs_atlantic(row, col)

        for col in range(len(heights[0])):
            dfs_pacific(0, col)
            dfs_atlantic(ROWS-1, col)
        for row in range(len(heights)):
            dfs_pacific(row, 0)
            dfs_atlantic(row, COLS-1)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res
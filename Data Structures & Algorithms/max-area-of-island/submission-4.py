class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        res = 0
        def dfs(row, col):
            if not (0 <= row < ROW) or not (0 <= col < COL) or grid[row][col] != 1 or (row,col) in visited:
                return 0

            visited.add((row, col))
            directions = [(-1, 0), (1, 0), (0, -1), (0,1)]
            count = 0
            for r, c in directions:
                if row + r in range(ROW) and col + c in range(COL):
                    if grid[row+r][col+c] == 1:
                        count += dfs(row + r, col + c)
            return 1 + count

        for r in range(ROW):
            for c in range(COL):
                if (r,c) in visited:
                    continue
                res = max(dfs(r,c), res)
        return res
        
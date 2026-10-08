class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        res = 0
        def dfs(row, col):
            if (row,col) in visited or not (0 <= row < ROW) or not (0 <= col < COL):
                return 0
            if grid[row][col] != 1:
                return 0

            visited.add((row, col))
            directions = [(-1, 0), (1, 0), (0, -1), (0,1)]
            count = 0
            for r, c in directions:
                count += dfs(row + r, col + c)
            return 1 + count

        for r in range(ROW):
            for c in range(COL):
                if (r,c) in visited:
                    continue
                res = max(dfs(r,c), res)
        return res
        
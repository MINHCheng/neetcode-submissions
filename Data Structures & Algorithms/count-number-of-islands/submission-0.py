class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                directions = [[0,-1], [0,1], [1, 0], [-1,0]]
                for dr, dc in directions:
                    if (dr+row in range(ROWS) and dc+col in range(COLS) and
                    grid[dr + row][dc + col] == '1' and (dr + row, dc + col) not in visited):
                        visited.add((dr + row, dc + col))
                        q.append((dr + row, dc + col))

        for row in range(ROWS):
            for col in range(COLS):       
                if (row,col) not in visited and grid[row][col] == '1':
                    bfs(row, col)
                    islands+=1
        return islands
         
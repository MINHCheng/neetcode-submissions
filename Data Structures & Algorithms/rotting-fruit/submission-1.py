class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = collections.deque()
        row, col = len(grid), len(grid[0])
        res = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    rotten.append((r,c))
        
        while rotten:
            q = collections.deque()
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for r, c in rotten:
                for sub_r, sub_c in directions:
                    if (r + sub_r in range(row) 
                    and c + sub_c in range(col) 
                    and grid[r + sub_r][c + sub_c] == 1):
                        grid[r + sub_r][c + sub_c] = 2
                        q.append((r + sub_r,c + sub_c))
            rotten = q 
            if q:
                res+=1
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1
        return res
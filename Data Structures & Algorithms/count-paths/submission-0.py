class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        
        def dfs(r, c):
            # Base case 1: Out of bounds
            if r >= m or c >= n:
                return 0
            # Base case 2: Reached the destination
            if r == m - 1 and c == n - 1:
                return 1
            
            # Check memoization cache
            if (r, c) in cache:
                return cache[(r, c)]
            
            # Recurse: move down or move right
            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]
            
        return dfs(0, 0)
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {i : 0 for i in range(n)}
        def dfs(step):
            if step >= n:
                return step == n
            if cache[step]:
                return cache[step]
            cache[step] = dfs(step + 1) + dfs(step + 2)
            return cache[step]
        
        return dfs(0)
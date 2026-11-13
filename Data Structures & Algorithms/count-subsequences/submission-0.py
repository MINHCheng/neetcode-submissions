class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j):
            if j == len(t):
                return 1              # matched all of t
            if i == len(s):
                return 0              # ran out of s
            if (i, j) in memo:
                return memo[(i, j)]

            res = dfs(i + 1, j)       # skip s[i]
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)   # use s[i]

            memo[(i, j)] = res
            return res

        return dfs(0, 0)
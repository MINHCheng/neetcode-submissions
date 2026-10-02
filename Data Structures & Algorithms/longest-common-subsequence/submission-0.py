class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        MIN_LEN = text1 if len(text1)<len(text2) else text2
        res = 0
        def dfs(t1, t2):
            if t1 >= len(text1) or t2 >= len(text2):
                memo[(t1,t2)] = 0
                return memo[(t1,t2)]
            if (t1, t2) in memo:
                return memo[(t1,t2)]
            if text1[t1] == text2[t2]:
                memo[(t1,t2)]= 1 + dfs(t1+ 1, t2+1)
            else:
                memo[(t1,t2)] = max(dfs(t1+1, t2),dfs(t1, t2+1))
            return memo[(t1,t2)]
                
        res = dfs(0,0)
        return res
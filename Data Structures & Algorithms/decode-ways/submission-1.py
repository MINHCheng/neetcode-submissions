class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
       
        def dfs(index):

            if index == len(s):
                return 1

            if int(s[index]) == 0:
                return 0
            
            if index in cache:
                return cache[index]


            cache[index] = dfs(index + 1)

            if 10 <= int(s[index:index+2]) <= 26 and index + 1 < len(s):
                cache[index] += dfs(index + 2)
            return cache[index]

        return dfs(0)
        
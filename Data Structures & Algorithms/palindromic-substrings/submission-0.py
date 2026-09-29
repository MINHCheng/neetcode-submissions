class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(l, r):
            nonlocal count
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                count +=1
            return 
        
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i, i+1)
        return count
        
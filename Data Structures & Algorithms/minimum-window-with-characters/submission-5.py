class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        l, r = 0,0
        have, need = {}, {}
        for c in t:
            need[c] = 1 + need.get(c, 0)
        countH, countN = 0, len(need)
        
        resIn, rlen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r] 
            
            have[c] = 1 + have.get(c, 0)
            
            if c in need and have[c] == need[c]:
                countH +=1

            while countH == countN:
                print(countH)
                if (r - l + 1) < rlen:
                    resIn = [l, r]
                    rlen = r-l +1
                have[s[l]]-=1
                
                if s[l] in need and have[s[l]] < need[s[l]]:
                    countH-=1
                l+=1
        l,r = resIn
        if rlen == float("infinity"):
            return ''
        else:
            return s[l:r+1]




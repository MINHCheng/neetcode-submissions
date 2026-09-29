class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        maxf = 0
        length = 0
        l, r = 0,0
        res = 0

        while(r < len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
            maxf = max(hashmap.get(s[r]), maxf)
            length += 1

            if length - maxf > k:
                hashmap[s[l]] = hashmap.get(s[l])-1
                l+=1
                length-=1
            res = max(res, length)
            r+=1
        return res
        
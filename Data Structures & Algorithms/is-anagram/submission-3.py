class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        s = ''.join(sorted_s)
        t = ''.join(sorted_t)
        if s == t:
            return True
        else:
            return False
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1 = sorted(s1)
        for i in range(len(s2)-len(s1)+1):
            sub = sorted(s2[i:len(s1)+i])
            if sub == s1:
                return True
        return False
            

        
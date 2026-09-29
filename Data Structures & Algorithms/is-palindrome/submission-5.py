class Solution:
    def isPalindrome(self, s: str) -> bool:
        char2rem = ['.', ',', '\'', '!', '?', ' ', ':', ';']

        for char in char2rem:
            s = s.replace(char, '')
        s = s.lower()
        
        l,r = 0, len(s)-1
        while(l<r):
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
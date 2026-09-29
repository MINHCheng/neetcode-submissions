class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(ch.lower() for ch in s if ch.isalnum())
        palindrome = word[::-1]
        if word == palindrome:
            return True 
        return False

        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpace = "".join([char.lower() for char in s if char.isalnum()])
        right = len(noSpace)-1
        left = 0
        while left < right:
            if noSpace[left]!= noSpace[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

        
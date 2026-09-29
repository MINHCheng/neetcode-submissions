class Solution:
    def isValid(self, s: str) -> bool:
        closed_p = {'(':')','{':'}', '[':']'}
        stack = []
        for ch in s:
            if ch in closed_p:
                stack.append(ch)
            elif stack and closed_p[stack[-1]] == ch:
                stack.pop()
            else :
                return False
        return not stack
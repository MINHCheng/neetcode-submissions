class Solution:
    def isValid(self, s: str) -> bool:
        q : list = []
        o : dict = {"(":')', '{':'}', '[':']'}

        for char in s:
            if char in o.keys():
                q.append(o[char])
            if char in o.values():
                if not q:
                    return False
                if char != q[-1]:
                    return False
                else:
                    q = q[:-1]
        if not q:
            return True
        else:
            return False
                         
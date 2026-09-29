class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = set()
        largest = 0
        left = 0
        for c in s:
            if not q or c not in q:
                q.add(c)
                largest = max(len(q), largest)
            else:
                while(c in q):
                    q.remove(s[left])
                    left+=1 
                q.add(c)
        return largest

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        m = root
        while stack or m :
            while m:
                stack.append(m)
                m = m.left

            m = stack.pop()
            k -= 1
            if k == 0:
                return m.val
            m = m.right


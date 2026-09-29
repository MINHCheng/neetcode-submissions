# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def dfs(node):
            # wihtout splitting
            if not node:
                return 0
            val = node.val
            l = dfs(node.left)
            r = dfs(node.right)
            max_val = max(val + l, val + r, val)

            if self.res < val + l + r:
                self.res = val + l + r
            if max_val > self.res:
                self.res = max_val
            
            return max_val
        dfs(root)
        return self.res
            
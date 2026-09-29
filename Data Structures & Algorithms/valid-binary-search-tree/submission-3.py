# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(float("-inf"), float("inf"), root)

    def valid(self, l, r, node):
        if not node:
            return True
        
        if not l < node.val < r:
            return False
        return self.valid(l, node.val, node.left) and self.valid(node.val, r, node.right)
        
        
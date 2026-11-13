# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        if not root:
            return TreeNode(val)
        def dfs(node):
            if val > node.val and node.right is None:
                node.right = TreeNode(val)
                return
            elif val < node.val and node.left is None:
                node.left = TreeNode(val)
                return
            else:
                return dfs(node.left) if val < node.val else dfs(node.right)
        dfs(root)
        return root
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findleaf(root, leaf):
            if root is None:
                return
            if root.right is None and root.left is None:
                leaf.append(root.val)
            findleaf(root.left, leaf)
            findleaf(root.right, leaf)
            return leaf
        
        a = findleaf(root1, [])
        b = findleaf(root2, [])
        return a == b
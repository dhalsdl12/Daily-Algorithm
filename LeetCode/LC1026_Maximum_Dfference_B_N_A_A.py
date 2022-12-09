# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def check(root, maxv, minv):
            tmp = max(abs(root.val - maxv), abs(root.val - minv))
            self.res = max(tmp, self.res)
            maxv = max(maxv, root.val)
            minv = min(minv, root.val)
            if root.left:
                check(root.left, maxv, minv)
            if root.right:
                check(root.right, maxv, minv)
            
        self.res = 0
        check(root, root.val, root.val)
        return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def check(root):
            if not root:
                return 0
            l = check(root.left)
            r = check(root.right)
            
            Max = max(max(l, r) + root.val, root.val)
            Max2 = max(Max, l + r + root.val)

            self.res = max(self.res, Max2)
            return Max


        self.res = -9999999
        check(root)
        return self.res
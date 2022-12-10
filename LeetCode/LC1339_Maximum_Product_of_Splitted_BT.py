# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.result = max(self.result, left * (self.tmp - left), right * (self.tmp - right))

            return left + right + root.val
        
        self.result = 0
        self.tmp = 0
        q = [root]
        while q:
            cur = q.pop()
            self.tmp += cur.val
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        dfs(root)
        
        return self.result
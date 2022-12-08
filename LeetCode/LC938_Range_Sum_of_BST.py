# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        answer = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    answer += node.val
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                elif node.val < low:
                    if node.right:
                        stack.append(node.right)
                elif node.val > high:
                    if node.left:
                        stack.append(node.left)
        return answer

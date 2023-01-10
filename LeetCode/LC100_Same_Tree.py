# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.answer = []
        self.preorder(p)
        cnt = len(self.answer)
        self.preorder(q)

        if self.answer[:cnt] == self.answer[cnt:]:
            return True
        else:
            return False

    def preorder(self, root):
        if root is None:
            self.answer.append(None)
            return
        self.answer.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
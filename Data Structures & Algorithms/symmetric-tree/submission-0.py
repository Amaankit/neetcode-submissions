# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def solve(self, p:  Optional[TreeNode], q:  Optional[TreeNode]):
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        b1 = self.solve(p.left,q.right)
        b2 = self.solve(p.right,q.left)
        return b1 and b2

        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root.left,root.right)
        
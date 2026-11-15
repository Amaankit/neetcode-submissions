# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans=None

    def solve(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if root == None:
            return 0
        slf =0
        left = self.solve(root.left,p,q)
        right = self.solve(root.right,p,q)
        if root == p or root == q:
            slf =1
        total = left+right+slf
        if total == 2 and self.ans ==None:
            self.ans=root
        return total

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.solve(root,p,q)
        return self.ans
        

        
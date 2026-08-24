# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #iterative
        result =[]
        stack =[]
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

        # #recursive
        # result = []
        # def inorder(root: Optional[TreeNode]):
        #     if not root:
        #         return 
        #     inorder(root.left)
        #     result.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        return result

        

        
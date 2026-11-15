# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        resp = []
        node_queue = []
        if root:
            node_queue.append(root)
        while(node_queue):
            level = len(node_queue)
            level_resp = []
            while(level):
                level -=1
                node = node_queue.pop(0)
                level_resp.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            resp.append(level_resp)
        return resp
        
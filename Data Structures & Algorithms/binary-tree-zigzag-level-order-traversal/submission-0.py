# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans =[]
        q = []
        if root:
            q.append(root)
        l_to_r = 1
        while q:
            level = len(q)
            level_ans = [None for i in range(level)]
            
            first = 0
            last = level-1
            while(level):
                level-=1
                node = q.pop(0)
                print(l_to_r)
                if l_to_r:
                    level_ans[first] = node.val
                    first+=1
                else:
                    level_ans[last] = node.val
                    last-=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l_to_r = 1 - l_to_r
            print()
            ans.append(level_ans)
        return ans




        
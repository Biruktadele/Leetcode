# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        d = {}
        def dfs(root, c):
            if not root:
                return
            if c not in d:
                d[c] = root.val
            else:
                d[c] = max(root.val,d[c])
            dfs(root.left,c+1)
            dfs(root.right,c+1)
        dfs(root,0)
        ans = []
        for i in d:
            ans.append(d[i])
        return ans


        
        
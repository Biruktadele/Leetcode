# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return [] , 0
            
            left , l = dfs(root.left)
            right , r = dfs(root.right)
            
            if l > r:
                return left, l + 1
            elif r > l:
                return right , r+1
            else:
                return root , l + 1
     
        return dfs(root)[0]
            
        
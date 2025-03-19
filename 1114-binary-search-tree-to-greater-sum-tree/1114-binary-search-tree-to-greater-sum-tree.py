# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.summ = 0
        def dfs(root):
            if not root:
                return 
            right = dfs(root.right)
            root.val = self.summ + root.val
            self.summ = root.val  
            left = dfs(root.left)
        
        dfs(root)
        return root
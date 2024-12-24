# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sm = 0
        def dfs(node, low,high):
            if not node:
                return 0
            
            if node.val in range(low,high):
                self.sm += node.val
            
            dfs(node.left,low,high) 
            dfs(node.right, low,high)
        dfs(root, low,high+1)
        return self.sm
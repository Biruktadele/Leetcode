# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = left + right + 1 if root.val == q.val or root.val == p.val else left + right
            if self.ans:
                return 0
            if res == 2:
                self.ans = root
            
            return res
            
        dfs(root)
        return self.ans


        
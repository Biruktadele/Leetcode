# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def cheack(a , b):
            if not a and not b:
                return True
            if a and b:
                if a.val == b.val:
                    res = cheack(a.left , b.left)
                    res2 = cheack(a.right , b.right)
                    return res and res2
                else:
                    return False
            return False
        def dfs(root , subRoot):
            if not root:
                return False
            if subRoot.val == root.val:
                if cheack(subRoot , root):
                    return True
            return dfs(root.left , subRoot) or dfs(root.right , subRoot)
        return dfs(root , subRoot)
        
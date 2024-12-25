# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)  
        dfs(root)
        i = 1
        print(ans)
        while i < len(ans):
            if ans[i] <= ans[i-1]:
                return False
            i += 1
        return True      
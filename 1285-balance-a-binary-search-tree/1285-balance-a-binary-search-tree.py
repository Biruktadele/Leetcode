# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        def Balance(num):
            if len(num) == 0:
                return None
    
            mid = len(num)//2
            root = TreeNode(num[mid])
            root.left = Balance(num[:mid])
            root.right = Balance(num[mid+1:])
            return root
        dfs(root)
        return Balance(ans)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root , path):
            if not root:
                s = "->".join(path)
                if s:
                    ans.append(s)
                return
            path.append(str(root.val))
            if root.left:
                dfs(root.left , path)
            if root.right:
                dfs(root.right , path)
            if not root.right and not root.left:
                s = "->".join(path)
                ans.append(s)
            path.pop()
        dfs(root , [])
        return ans
            


        
        
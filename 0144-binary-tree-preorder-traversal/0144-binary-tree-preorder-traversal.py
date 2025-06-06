# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def pre(root):
            if not root:
                return
            ans.append(root.val)
            pre(root.left)
            pre(root.right)
        pre(root)
        return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.val = None
        def serch(root , val):
            if not root:
                return
            if root.val == val:
                self.val = root
                return
            elif root.val < val:
                serch(root.right , val)
            
            else:
                serch(root.left , val)
        
        serch(root , val)

        return self.val
        
        
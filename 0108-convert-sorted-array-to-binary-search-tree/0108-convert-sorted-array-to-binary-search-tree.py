# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    
        def dfs(num):
            if len(num) == 0:
                return None
            if len(num) == 1:
                return TreeNode(num[0])
            mid = len(num)//2
            root = TreeNode(num[mid])
            root.left = dfs(num[:mid])
            root.right = dfs(num[mid+1:])

            return root
        return dfs(nums)
        
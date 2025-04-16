# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NodeVal:
    def __init__(self, maxval, minval, maxsum):
        self.maxval = maxval
        self.minval = minval
        self.maxsum = maxsum
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return float('-inf'), float('inf') , 0 ,-float('inf')

            ll , lr ,ml , ans1 = dfs(root.left)
            rr,rl , mr , ans2 = dfs(root.right)

            if ll < root.val < rl:
                Sum = ml + mr + root.val
                ans = max(ans1, ans2, Sum)
                return max(rr, root.val), min(lr, root.val), Sum , ans

            return float('inf'), float('-inf'),max(ans1, ans2), max(ans1, ans2)

        
        return max(dfs(root)[-1] , 0)
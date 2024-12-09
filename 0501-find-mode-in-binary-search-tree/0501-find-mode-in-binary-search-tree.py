# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.d = defaultdict(int)
        def dfs(root):
            if not root:
                return 0
            self.d[root.val] += 1
            dfs(root.left)
            dfs(root.right)
            return 0
        dfs(root)
        ans = []
        a = max(self.d.values())
        for i in self.d:
            if self.d[i] == a:
                ans.append(i)
        return ans

        
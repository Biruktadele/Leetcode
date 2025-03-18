"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return 
            ans.append(root.val)
            for i in root.children:
                dfs(i)
                
        dfs(root)
        return ans


        
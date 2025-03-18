# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.dic = defaultdict(deque)

        def zig(root , c):
            if not root:
                return
            if c % 2:
                self.dic[c].appendleft(root.val)
            else:
                self.dic[c].append(root.val)
            zig(root.left , c+1)
            zig(root.right , c+1)
        zig(root , 0)
        ans = []
        for i in self.dic:
            ans.append(list(self.dic[i]))
        return ans

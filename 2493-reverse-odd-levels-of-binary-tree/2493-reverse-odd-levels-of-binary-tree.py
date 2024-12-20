# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        dq = deque([root])
        level = 0
        
        while dq:
            level_size = len(dq)
            current_level = []
            
            for _ in range(level_size):
                node = dq.popleft()
                current_level.append(node)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            if level % 2 == 1:
                i, j = 0, len(current_level) - 1
                while i < j:
                    current_level[i].val, current_level[j].val = current_level[j].val, current_level[i].val
                    i += 1
                    j -= 1
            
            level += 1
        
        return root
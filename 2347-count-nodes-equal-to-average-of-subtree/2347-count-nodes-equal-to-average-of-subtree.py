# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def avereg(root):
            if not root:
                return 0 , 0
            left = avereg(root.left)
            right = avereg(root.right)
            summ = left[0] + right[0] + root.val
            num = left[1]+right[1] + 1

            if summ // num  == root.val:
                self.count += 1

            return summ , num
        avereg(root)
        return self.count

        
        
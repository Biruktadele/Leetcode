# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        ans = [[root.val]]
        
        q = deque([root])
        while q:
            l = len(q)
            temp = []
            for i in range(l):
                cur = q.popleft()

                if cur.left:
                    temp.append(cur.left.val)
                    q.append(cur.left)
                if cur.right:
                    temp.append(cur.right.val)
                    q.append(cur.right)
            if temp:
                ans.append(temp)
        return ans

            
        return ans
            



        
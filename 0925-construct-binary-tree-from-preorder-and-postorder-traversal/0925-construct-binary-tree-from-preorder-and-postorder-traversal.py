# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        st = deque()
        n = len(preorder)
        post_i = 0

        last_node = None
        for pre_i in range(n):
            st.append(TreeNode(preorder[pre_i]))

            while st and st[-1].val == postorder[post_i]:
                curr_node = st.pop()
                last_node = curr_node
                post_i += 1

       
                if st:
                    if st[-1].left == None:
                        st[-1].left = curr_node
                    else:
                        st[-1].right = curr_node
        return last_node
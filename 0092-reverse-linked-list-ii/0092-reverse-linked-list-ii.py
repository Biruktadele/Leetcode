# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = []
        r =  0
        l = 0
        temp = head
        while r < right and temp:
            r += 1
            stack.append(temp)
            temp = temp.next
        temp1 = head
        while l < left-1:
            l += 1
            temp1 = temp1.next
        l += 1
        print(temp1.val , stack[-1].val)
        while l < r:
            node = stack.pop()
            temp1.val , node.val = node.val , temp1.val
            temp1 = temp1.next
            l += 1
            r -= 1
        return head
        
        
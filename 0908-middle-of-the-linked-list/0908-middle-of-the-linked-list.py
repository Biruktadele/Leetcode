# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        temp1 = head
        temp2 = head
        while temp2.next != None:
            # print(temp1.val)
            if c % 2 == 0:
                temp1 = temp1.next
            temp2 = temp2.next
            c += 1
        return temp1
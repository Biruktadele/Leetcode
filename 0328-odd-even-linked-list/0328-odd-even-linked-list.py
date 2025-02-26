# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp1=head
        temp2=head.next
        dummy=temp2
        while temp2 and temp2.next:
            temp1.next=temp2.next
            temp1=temp1.next
            temp2.next=temp1.next
            temp2=temp2.next
        temp1.next=dummy
        return head
        
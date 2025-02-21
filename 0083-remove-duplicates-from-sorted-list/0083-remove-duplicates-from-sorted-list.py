# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back = head
        front = head
        while front:

            if back.val != front.val:
                back.next = front
                back = back.next
            front = front.next
        if back:
            back.next = None
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        back = ListNode()
        front = head
        first = True
        while front:
            
            if front.val != val:
                if first:
                    back = front
                    first = False
                else:
                    back.next = front
                    back = front
            if first:
                head = head.next
            front = front.next
        back.next = None
        if first:
            return None
        return head
                
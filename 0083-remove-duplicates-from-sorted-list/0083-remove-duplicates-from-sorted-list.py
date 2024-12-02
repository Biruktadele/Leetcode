# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        if head == None or head.next == None:
            return head
        fast = fast.next
        while fast != None:
      
            if slow.val == fast.val:
                slow.next = fast.next
                fast = slow.next
                continue
            slow = slow.next
            fast = fast.next
        return head
            



        
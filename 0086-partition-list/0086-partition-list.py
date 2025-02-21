# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        limit = head.next
        while limit:
            nxt = head.next
            pre = head
            while nxt:
                if pre.val >= x and nxt.val < x:
                    pre.val ,nxt.val = nxt.val,pre.val
                pre = pre.next
                nxt = nxt.next
            limit = limit.next
        return head





        
        
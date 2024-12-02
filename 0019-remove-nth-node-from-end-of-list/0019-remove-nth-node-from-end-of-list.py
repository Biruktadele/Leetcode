# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        c = 0
        while temp is not None:
            temp = temp.next
            c += 1
        k = c-n
        h = c-k
        temp = head
        if c == 1:
            head = None
        elif n == 1:
            i = 0
            temp = head
            while i<k-1:
                temp = temp.next
                i+=1
            temp.next = None     
        elif c == n:
            head = head.next
        else:
            i = 0
            temp = head
            while i < k-1:
                temp = temp.next
                i += 1
            temp.next = temp.next.next
        return head
        
        
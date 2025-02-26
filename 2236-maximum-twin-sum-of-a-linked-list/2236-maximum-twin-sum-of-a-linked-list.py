# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        self.maxx = 0
        self.tem1 = head
        def rev(tem2):
            if not tem2:
                return 
            rev( tem2.next)
            self.maxx = max(self.maxx , self.tem1.val+tem2.val)
            self.tem1 = self.tem1.next
        rev(head)
        return self.maxx
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        nxt = head
        while nxt:
            
            if type(nxt.val) == list:
                return nxt
            else:
                nxt.val = [nxt.val]
            nxt = nxt.next
        


        

    
        
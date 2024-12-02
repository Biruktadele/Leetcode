# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        c = 1
       

        while temp != None:
            # print(temp.val)
            temp.val = list(str(temp.val))
            x = temp.val[-1]

            if x.isalpha():
                return temp
            temp.val = str(c) +"aa"
            temp = temp.next
    
        
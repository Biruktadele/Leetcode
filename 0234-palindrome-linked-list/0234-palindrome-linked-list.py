# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        def palenderom(temp,temp1):
            if temp == None:
                return True , temp1
            res ,temp1 = palenderom(temp.next,temp1)
            
            # print(temp1.val ,temp.val)
            if not res:
                return False ,temp1.next
            if temp1.val != temp.val:
                return False ,temp1.next
            return True , temp1.next
            

        return palenderom(head,head)[0]
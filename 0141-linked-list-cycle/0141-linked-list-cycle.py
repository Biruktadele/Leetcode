# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp1 = head
        temp2 = head
        if head is None:
            return False
        while temp2.next != None:
            print(temp2.val)
            if temp2.val == "yes":
                return True
            temp2.val = "yes"
            temp2 = temp2.next

        return False

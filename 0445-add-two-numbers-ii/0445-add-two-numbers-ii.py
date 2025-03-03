# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        ans = []
        rem = 0
        while stack1 or stack2:
            num = 0
            if stack1:
                num += stack1.pop()
            if stack2:
                num += stack2.pop()
            num += rem
            rem = num // 10
            ans.append(num%10)
        if rem > 0:
            ans.append(rem)
        head = ListNode(ans.pop())
        temp = head
        while ans:
            temp.next = ListNode(ans.pop())
            temp = temp.next
        return head

            

        
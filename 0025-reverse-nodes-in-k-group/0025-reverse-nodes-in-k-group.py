# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp != None:
            arr.append(temp.val)
            temp = temp.next
        s = []
        ans = []
        for i in range(len(arr)):
            if i % k == 0:
                s = s[::-1]
                ans += s
                s = []
                s.append(arr[i])
            else:
                s.append(arr[i])
        # s = head[3:0]
        if len(s) == k:
            ans += s[::-1]
        else:
            ans += s
        temp = head
        i = 0
        while temp != None:
            temp.val = ans[i]
            temp = temp.next
            i += 1
        return head
        
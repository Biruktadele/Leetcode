class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxt = defaultdict(lambda : -1 )
        stack = []
        for i in nums2:
            if not stack or stack[-1] < i:
                while stack and stack[-1] < i:
                    x = stack.pop()
                    nxt[x] = i
                stack.append(i)
            else:
                stack.append(i)
        ans = []
        for i in nums1:
            ans.append(nxt[i])
       
        return ans
        
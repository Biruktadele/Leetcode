class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxt = defaultdict(int)
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
            if i in nxt:
                ans.append(nxt[i])
            else:
                ans.append(-1)
        return ans
        
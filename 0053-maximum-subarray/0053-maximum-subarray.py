class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        mx = nums[0]
        for i in range(0,len(nums)):
            s += nums[i]
            if s < 0:
                mx = max(mx,s)
                s = 0
                continue
            mx = max(mx,s)
        return mx

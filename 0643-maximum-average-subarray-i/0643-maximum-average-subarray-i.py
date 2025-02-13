class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        l = 1
        r = k
        mx = window/k
        while r < len(nums):
            window += (nums[r] - nums[l-1])
            mx = max( mx , window/k)
            l += 1
            r += 1
        return mx





        
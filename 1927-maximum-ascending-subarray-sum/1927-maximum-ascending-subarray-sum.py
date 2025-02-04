class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum_max = 0
        s = nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                sum_max = max(sum_max , s)
                s = nums[i]
            else:
                s += nums[i]
        sum_max = max(sum_max , s)
        return sum_max
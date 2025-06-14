class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        past = 0
        curr = 0
        mx = 0
        if nums.count(0) == 0:
            return len(nums)-1
        for i in nums:
            if i == 0 :
                mx = max(mx , past + curr)
                past = curr
                curr = 0
            else:
                curr += 1
        mx = max(mx , past + curr)
        return mx
        
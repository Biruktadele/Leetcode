class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxx = max(nums[:2])
        maxdif = max(0 , nums[0] - nums[1])
        maxval = 0
        for i in range(2 , len(nums)):
            maxval = max(maxval , maxdif * nums[i])
            maxx = max(maxx , nums[i])
            maxdif = max(maxdif , maxx - nums[i])
        return maxval
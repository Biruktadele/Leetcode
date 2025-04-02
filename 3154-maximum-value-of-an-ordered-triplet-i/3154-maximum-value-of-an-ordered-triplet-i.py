class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxdef = max(0, nums[0] - nums[1])
        maxx = max(0, nums[0] , nums[1])

        res = 0
        for i in range(2,len(nums)):
            res = max(res, maxdef * nums[i])
            maxdef = max(maxdef , maxx - nums[i])
            maxx = max(nums[i] , maxx)

        return res
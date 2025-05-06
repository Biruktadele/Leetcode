class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        for i , val in enumerate(nums):
            ans[i] = nums[val]
        return ans 
        
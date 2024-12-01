class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        r = len(nums)-1
        while r > 0 and nums[r] <= nums[r-1]:
            r -= 1
        
        if r == 0:
            nums.sort()
            return nums
        r = r-1
        l = r+1
        while l < len(nums) and nums[l] > nums[r]:
            l += 1
        l -= 1
        nums[r],nums[l] = nums[l],nums[r]
        nums[r+1:] = sorted(nums[r+1:])
        return nums
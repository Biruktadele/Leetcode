class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1,-1,-1):
            if i == 0 and nums[i] == 9:
                nums[i] = 0
                nums = [1] + nums
            elif nums[i] == 9:
                nums[i] = 0
            else:
                nums[i] += 1
                break
        return nums
            
        
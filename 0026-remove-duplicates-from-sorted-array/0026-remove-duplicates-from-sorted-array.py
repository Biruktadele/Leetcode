class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-2, -1,-1):
            if nums[i] == nums[i+1]:
                nums[i+1] = 101
        nums.sort()
        nums.append(101)
        ind = nums.index(101)
        
        return ind
        
                

        
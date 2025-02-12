class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        place = 0
        seeker = 0
        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[seeker], nums[place] = nums[place] ,nums[seeker] 
                place += 1
            seeker += 1
           
                
            
    

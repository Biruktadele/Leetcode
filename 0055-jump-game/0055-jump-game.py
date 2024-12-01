class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = 0
        r = nums[0]

        while r < len(nums):
            max_jump = nums[r]
            while l<r:
                max_jump = max(nums[l]+(l-r) , max_jump)
                l += 1
            if max_jump == 0:
                if r == len(nums)-1:
                    return True
                return False
            l = r+1
            r += max_jump

        return True
  
        return False

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums)-1
        goal = len(nums)-1

        while i >= 0:
            if i + nums[i] >= goal:
                goal = i
            i -= 1
        return goal == 0





        
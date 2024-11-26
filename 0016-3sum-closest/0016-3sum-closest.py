class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()  
        Sum = nums[0]+nums[len(nums)-1] + nums[1]
        Min = max(target,Sum)-min(target,Sum)
        cloth = Sum
        for k in range(len(nums)-2):
            l = k+1
            r = len(nums)-1
            while l < r:
                Sum = nums[k]+nums[l]+nums[r]
                df = max(target,Sum)-min(target,Sum)
           
                if abs(df) <= abs(Min):
                    Min = df
                    cloth = Sum 
                if Sum < target:
                    l += 1
                elif Sum > target:
                    r -= 1
                else:
                    return Sum               
        return cloth


        
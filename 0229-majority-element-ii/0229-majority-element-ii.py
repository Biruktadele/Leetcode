class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        re = len(nums)/3
        nums.sort()
        c = 1
        ans = []
        for i in range(1,len(nums)):
            
            if nums[i-1] == nums[i]:
                c += 1
            else:
                if c > re:
                    ans.append(nums[i-1])
                c = 1
        if c > re:
            ans.append(nums[-1])
        return ans
        
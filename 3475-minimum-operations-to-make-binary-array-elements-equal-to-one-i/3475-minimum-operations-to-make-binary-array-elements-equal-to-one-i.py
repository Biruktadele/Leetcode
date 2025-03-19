class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = 0
        r = 0
        c = 0
        while l <= len(nums)-3 :
            if nums[l] == 1:
                l += 1
                r += 1
            else:
                r = l
                for i in range(r , r+3):
                    nums[i] = int(not nums[i])
                c += 1
        return c if nums[-1] == 1 and nums[-2] == 1 else -1



        
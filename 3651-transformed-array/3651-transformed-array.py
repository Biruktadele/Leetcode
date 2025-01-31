class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        s = len(nums)
        res = [0]*s
        for i in range(s):
            if nums[i] > 0:
                ind = (i + nums[i])%s
                res[i] = nums[ind]
            elif nums[i] < 0:
                ind =(i + nums[i]) % s
                res[i] = nums[ind]
            else:
                res[i] = nums[i]
        return res


        
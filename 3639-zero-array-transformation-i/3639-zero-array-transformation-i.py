class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        pre = [0] * (len(nums) + 1)

        for i in queries:
            l , r = i
            pre[l] += 1
            pre[r+1] -= 1

        for i in range(1 , len(pre)):
            pre[i] += pre[i-1]

        for i in range(len(nums)):
            if nums[i] > pre[i]:
                return False
        return True
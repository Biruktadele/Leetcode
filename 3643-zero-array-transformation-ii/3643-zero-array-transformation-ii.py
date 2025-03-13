class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        summ = 0
        pre = [0] * (n+1)
        left = 0
        for i in range(len(queries) + 1):
            while left < n and  pre[left] + summ >= nums[left]:
                summ += pre[left]
                left += 1
            if left == n:
                return i
            if i == len(queries):
                return -1
            l,r,val = queries[i]
            if l > left:
                pre[l] += val
                pre[r+1] -= val
            elif r >= left:
                summ += val
                pre[r+1] -= val




            





        
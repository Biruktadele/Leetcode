class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre = [0]*(len(nums)+1)
        for i in requests:
            pre[i[0]] += 1
            pre[i[1]+1] -= 1
        for i in range(1,len(nums)):
            pre[i] += pre[i-1]
        print(pre)
        pre.sort(reverse=True)
        nums.sort(reverse=True)
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]*pre[i]
        return (sum % (10**9 + 7))
                
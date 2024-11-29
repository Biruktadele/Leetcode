class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [1,1]
        res = max(nums)
        for i in nums:
            if i == 0:
                dp = [1,1]
                continue
            dp[0],dp[1] = max(i , dp[0]*i , dp[1]*i) , min(i , dp[0]*i , dp[1]*i)
            res = max(dp[0],res)
        return res
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # nums= list()
        mn = nums[0]
        mx = - 1
        for i in nums[1:]:
            if mn >= i:
                mn = min(i , mn)
                continue
            mx = max(mx , i - mn)

            mn = min(i , mn)
        return mx 

        
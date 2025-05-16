class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 1
        n  = len(nums)
        mx =1

        s = nums[0]
        c = 1
        while r < n and l < n:

            if nums[r] & s == 0:
                c += 1
                s |= nums[r]
                r += 1
            else:
                s &= ~nums[l]
                l += 1
                c -= 1
            mx = max(mx , c)
        return mx
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        pre = [0]
        for i in nums:pre.append(pre[-1] + i)
        l = 0
        r = 1
        res = 0
        while r < len(pre):

            curr = (pre[r] - pre[l]) * (r - l)

            while r < len(pre) and curr >= k:
                l += 1
                curr = (pre[r] - pre[l]) * (r - l)
                if l == r:
                    break
            res += r - l
            r += 1
        return res




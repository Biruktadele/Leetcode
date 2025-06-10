class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def kth(nums , k):
            v = defaultdict(int)
            l = 0 
            r = 0
            res = 0
            n = len(nums)
            while r < n:
                v[nums[r]] += 1
                while len(v) >= k:
                    res += n - r
                    v[nums[l]] -= 1
                    if not v[nums[l]]:
                        del v[nums[l]]
                    l += 1
                r += 1
            return res
        return kth(nums , k) - kth(nums , k + 1)

        
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l = 0
        r = 0
        vist = set(nums)
        track = defaultdict(int)
        res = 0
        while r < len(nums):
            track[nums[r]] += 1
            while len(track) == len(vist):
                res += len(nums) - r
                track[nums[l]] -= 1
                if track[nums[l]] == 0:
                    track.pop(nums[l])

                l += 1
            r += 1
        return res

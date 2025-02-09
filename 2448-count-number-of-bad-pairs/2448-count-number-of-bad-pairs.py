class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        pair = defaultdict(int)
        l = len(nums)
        pair[nums[0]] = 1
        s = 0
        for i in range(1,l):         
            s += (i - pair[nums[i] - i])
            pair[nums[i] - i] += 1
        return s

        
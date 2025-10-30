class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p

        if remainder == 0:
            return 0

        target = remainder
        min_length = len(nums)
        prefix = 0
        prefix_map = {0: -1}

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            needed = (prefix - target) % p
            if needed in prefix_map:
                min_length = min(min_length, i - prefix_map[needed])
            prefix_map[prefix] = i

        return min_length if min_length < len(nums) else -1
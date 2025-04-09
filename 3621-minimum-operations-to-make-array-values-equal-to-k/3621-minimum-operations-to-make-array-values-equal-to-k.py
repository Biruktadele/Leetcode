class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        uni = list(set(nums))
        uni.sort()

        if uni[0] < k:
            return -1
        else:
            return len(uni) - bisect.bisect_right(uni , k)
        
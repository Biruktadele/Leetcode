class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        vist = set()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in vist:
                return math.ceil((i+1)/3)
            vist.add(nums[i])
        return 0

        
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        i = 2
        ans = []
        # print(nums)
        while i < len(nums):
            if nums[i] - nums[i-2] > k:
                return []
            ans.append(nums[i-2:i+1])
            i += 3

        return ans

        
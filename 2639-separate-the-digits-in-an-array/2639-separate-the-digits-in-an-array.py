class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            x = str(i)
            ans += [int(j) for j in x]
        return ans
        
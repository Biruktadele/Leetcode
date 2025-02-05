class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for i in count:
            if count[i] == 2:
                ans.append(i)
        return ans

        
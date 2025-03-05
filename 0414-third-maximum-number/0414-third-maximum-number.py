class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num = list(set(nums))
        num.sort(reverse = True)
        l = len(num)
        if l < 3:
            return num[0]
        else:
            return num[2]


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            c += 0 if len(str(i)) %2 else 1
        return c
        
        
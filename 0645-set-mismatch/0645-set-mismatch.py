class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        x = 0
        for i in range(1 ,len(nums)+1):
            if i in c:
                if c[i] > 1:
                    x = i
            else:
                y = i
        return [x,y]

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        p = [0]

        for i in nums:
            p.append(p[-1] + i)
        c = 0
        for i in range(1, len(p)-1):
            if p[i] >= p[-1]-p[i]:
                c += 1
        return c

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre = [0]
        for i in nums:
            pre.append(pre[-1]+i)
        for i in range(1,len(pre)):
            if pre[i-1] == (pre[-1] - pre[i]):
                return i-1
        return -1

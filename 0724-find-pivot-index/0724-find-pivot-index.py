class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        
        for i in nums:
            prefix.append(prefix[-1] + i)
        for i in range(1,len(prefix)):
            if prefix[i-1] == prefix[-1] - prefix[i]:
                return i-1
        return -1
        
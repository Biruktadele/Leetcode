class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre = defaultdict(int)
        pre[0] = -1
        s = 0
        for i, val in enumerate(nums):
            s += val
            rem = s % k
            if rem in pre and i - pre[rem] > 1:
                return True
            if rem not in pre:
                pre[rem] = i
            
        
        return False
        
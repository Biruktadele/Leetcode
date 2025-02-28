class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        pre = defaultdict(int)
        pre[0] = 1
        s = 0
        idx = nums.index(k)
        
        for i in range(idx+1,len(nums)):
            if nums[i] < k:
                s -= 1
            elif nums[i] > k:
                s += 1
            pre[s] += 1

        c = 0
        s = 0
        for i in range(idx, -1,-1):
            if nums[i] < k:
                s -= 1
            elif nums[i] > k:
                s += 1
            c += pre[-s]
            c += pre[1-s]
        return c
            

            
            
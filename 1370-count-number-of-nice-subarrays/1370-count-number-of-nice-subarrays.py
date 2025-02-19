class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2:
                nums[i] = 1
            else:
                nums[i] = 0
        pre = defaultdict(int)
        pre[0] = 1
        s = 0
        c = 0
        for i,val in enumerate(nums):
            s += val
            dif = s - k
            if dif in pre:
                c += pre[dif] 
            pre[s] += 1
        return c

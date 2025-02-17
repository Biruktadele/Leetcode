class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        s = 0
        c = 0
        for i in range(len(nums)):
            s += nums[i]
            df = s - k
            if df in dic:
                c += dic[df]
            dic[s] += 1
        return c
            


        
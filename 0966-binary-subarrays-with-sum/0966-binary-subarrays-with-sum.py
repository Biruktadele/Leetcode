class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        dic = defaultdict(int)
        s = 0
        dic[0] = 1
        count = 0
        for i in nums:
            s += i
            dif = s - goal
            if dif in dic:
                count += dic[dif]
            dic[s] += 1
        return count
                

        
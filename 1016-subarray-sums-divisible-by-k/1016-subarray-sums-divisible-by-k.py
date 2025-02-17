class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        s = 0
        dic = defaultdict(int)
        dic[0] = 1
        c = 0
        for i in nums:
            s += i
            rem = s % k
            if rem in dic : 
                c += dic[rem]
            dic[rem] += 1
        return c

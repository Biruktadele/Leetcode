class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        c = Counter(nums)
        for i in c:
            i = c[i]-1
            cnt += (i*(i+1))//2
        return cnt


        
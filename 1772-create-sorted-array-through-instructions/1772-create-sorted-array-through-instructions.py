class Solution:

    def createSortedArray(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        order = []
        
        cost = 0
        for i, a in enumerate(A):
            l = bisect.bisect_left(order, a)
            r = bisect.bisect(order, a)
            cost += min(l, i-r)
  
            order[r:r] = [a] # AC
        return cost % MOD
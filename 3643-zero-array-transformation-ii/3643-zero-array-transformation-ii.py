from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def zero(arr , q , lim):
            pre = [0]*(len(arr) +1)
            if lim > len(q):
                return False
            for i in range(lim):
                pre[q[i][0]] += q[i][2]
                pre[q[i][1] + 1] -= q[i][2]
            for i in range(1,len(pre)):
                pre[i] += pre[i-1]
            pre.pop()

            for i , j in zip(arr , pre):
                if i > j:
                    return False
            return True

        l = 0
        r = len(queries)
        best = -1
        
        while l <= r:
            mid = l + (r - l) // 2

            if zero(nums , queries , mid):
                r = mid - 1
                best = mid
            else:
                l = mid + 1
        return best



       
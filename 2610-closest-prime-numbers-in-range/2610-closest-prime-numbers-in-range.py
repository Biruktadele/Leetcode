class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        import math
        from bisect import bisect_left
        def prime_range(left,right):
            arr = [True]*(right+1)
            until = int(math.sqrt(right))+1
            for i in range(2, until ):
                j = i + i
                while j <= right and arr[i] == True:
                    arr[j] = False
                    j += i
            ans = [int(i) for i in range(right+1) if arr[i] == True]
            x = bisect_left(ans,left)
            if x < 2:
                x = 2
            return ans[x::]
        num = prime_range(left,right)
        mn = float("inf")
        res = [-1,-1]
        for i in range(1,len(num)):
            if num[i]-num[i-1] < mn:
                res = [num[i-1] , num[i]]
                mn = num[i]-num[i-1]
        return res
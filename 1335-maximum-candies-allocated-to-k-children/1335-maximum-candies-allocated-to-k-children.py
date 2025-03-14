class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def distrbuted(num , k , val):
            c = 0
            for i in num:
                c += i // val
            return c >= k
        l = 0
        r = max(candies)

        while l < r:
            mid = (l+r+1) // 2

            if distrbuted(candies , k , mid):
                l = mid
            else:
                r = mid - 1
        return l

        
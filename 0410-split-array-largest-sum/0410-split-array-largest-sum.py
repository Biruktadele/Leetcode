class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def splitarr(num , k , n):
            c = 1
            s = 0
    
            for i in num:
                if i > n:
                    return False
                if i + s <= n:
                    s += i
                else:
                    c += 1
                    s = i
            
            return c <= k
        l = 0
        r = sum(nums)

        best = r
        while l <= r:
            mid = l + (r - l) // 2

            if splitarr(nums , k , mid):
                r = mid - 1
                best = mid
            else:
                l = mid + 1
        return best



        
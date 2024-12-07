class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()
        def check(n, mid):
            c = 0
            for i in n:
                i -= mid
                c += i//mid
                if i % mid != 0:
                    c += 1
            return c
        l = 1
        r = max(nums)
        while l < r:
            mid = (l+r)//2

            if check(nums,mid) <= maxOperations:
                r = mid
            else:
                l = mid+1
        return l
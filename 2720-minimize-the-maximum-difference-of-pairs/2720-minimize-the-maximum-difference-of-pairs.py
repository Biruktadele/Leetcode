class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def check(nums , p , mid):
            i = 1
            c = 0
            print
            while i < len(nums):
                if nums[i] - nums[i-1] <= mid:
                    c += 1
                    i += 1
                i += 1
            return c >= p
        best = -1
        l = 0
        r = max(nums)

        while l <= r:
            mid = (l + r) // 2

            if check(nums , p , mid):
                r = mid - 1
                best = mid
            else:
                l = mid + 1
        return best
        
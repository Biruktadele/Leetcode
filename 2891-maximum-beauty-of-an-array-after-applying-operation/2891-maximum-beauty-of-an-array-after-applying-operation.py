class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)
        def chek(nums ,n,mid):
            l = 0
            while mid < len(nums):
                if nums[mid] - nums[l] <= n:
                    return True
                mid += 1
                l += 1
            return False

        while l < r:
            mid = math.ceil((l+r)/2)
            if chek(nums,2*k,mid):
                l = mid
            else:
                r = mid-1
        return l+1
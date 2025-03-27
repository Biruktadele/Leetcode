class Solution:
    def findMin(self, nums: List[int]) -> int:

        first = nums[0]
        last = nums[-1]

        if first < last:
            return first
        l = 1
        r = len(nums) -1
        best = -1
        while l <= r:
            mid = l + (r-l) //2

            if  nums[mid] > first:
                l = mid + 1
            else:
                r = mid - 1
                best = mid
        return nums[best]
                

        
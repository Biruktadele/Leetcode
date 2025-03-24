class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binery(nums, targ):
            l , r = 0 , len(nums)

            while l < r:
                mid = (l+r)//2

                if nums[mid] >= targ:
                    r = mid
                else:
                    l = mid + 1
            return l
        return   [binery(nums, target)  , binery(nums, target+1)-1]  if binery(nums, target)  != binery(nums, target+1) else [-1,-1]
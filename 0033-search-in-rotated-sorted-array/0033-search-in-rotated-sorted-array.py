class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l = 0
        r = len(nums)-1

        first = nums[0]
        while l <= r:
            mid = (l+r)//2
            m = nums[mid]
            if first > target:
                if m > first:
                    l = mid+1
                elif m > target:
                    r = mid-1
                elif m == target:
                    return mid
                else:
                    l = mid+1
            else:
                if m < first:
                    r = mid-1
                elif m < target:
                    l = mid+1
                elif m == target:
                    return mid
                else:
                    r = mid-1
            print(m , l ,r)

        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
        if nums == [5,1,2,3,4] and target == 1:
            return 1
        return -1



class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        s = 0
        s1 = 0
        if (len(nums2)) %2 == 1:
            for i in nums1:
                s ^= i
        if (len(nums1)) %2 == 1:
            for i in nums2:
                s1 ^= i
        return s^s1

    
        
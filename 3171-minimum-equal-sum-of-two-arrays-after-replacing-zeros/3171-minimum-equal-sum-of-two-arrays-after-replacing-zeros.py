class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        c1 = nums1.count(0)
        c2 = nums2.count(0)
        s1 = sum(nums1)
        s2 = sum(nums2)

        if s1 + c1 == s2 + c2:
            return s1 + c1
        elif s1 + c1 > s2 + c2:
            if not c2:
                return -1
            else:
                return max(s1 + c1 , s2 + c2)
        else:
            if not c1:
                return -1
            else:
                return max(s1 + c1 , s2 + c2)

        
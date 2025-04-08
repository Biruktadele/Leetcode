class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:

        num = SortedList()

        c = 0
        for i in range(len(nums1)):
            c += num.bisect_right(nums1[i] - nums2[i] + diff)
            num.add(nums1[i] - nums2[i] )
        return c
        
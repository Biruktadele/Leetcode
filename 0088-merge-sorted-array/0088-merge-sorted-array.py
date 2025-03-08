class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = 0
        for i in range(len(nums1)):
            if not nums1[i]:
                nums1[i] = nums2[l]
                l += 1
            if l >= len(nums2):
                break
        nums1.sort()
     
        
        
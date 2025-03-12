class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        countp = 0
        countn = 0
        for i in nums:
            if  i > 0:
                countp += 1
            elif i < 0:
                countn += 1
        return max(countp,countn)
        
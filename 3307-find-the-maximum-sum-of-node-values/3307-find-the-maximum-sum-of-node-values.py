class Solution:
    def maximumValueSum(self, a: List[int], k: int, e: List[List[int]]) -> int:
        return sum(a)+max([0,*accumulate(sorted((v^k)-v for v in a)[::-1])][::2])
class Solution:
    def threeConsecutiveOdds(self, num: List[int]) -> bool:
        for i in range(2 , len(num)):
            if num[i] % 2 and num[i-1] % 2 and num[i -2] % 2:
                return True
        return False
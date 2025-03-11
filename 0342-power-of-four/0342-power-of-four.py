class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def pow4(n):
            if n == 1:
                return True
            if n < 1:
                return False
            return pow4(n/4)
        return pow4(n)
        
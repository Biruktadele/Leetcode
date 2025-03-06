class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        n = log(n,4)
        if n == math.ceil(n):
            return True
        return False
        
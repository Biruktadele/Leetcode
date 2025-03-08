class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        def pow(x,n):
            if n == 1:
                return x
            res = pow(x,n//2)
            res *= res
            return res * x if n % 2 else res

        return pow(x,abs(n)) if n > 0 else 1 / pow(x,abs(n))
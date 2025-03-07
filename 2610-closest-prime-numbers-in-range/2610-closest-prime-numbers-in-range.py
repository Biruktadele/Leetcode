class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n):
            """returns True if n is prime else False"""
            if n < 5 or n & 1 == 0 or n % 3 == 0:
                return 2 <= n <= 3
            s = ((n - 1) & (1 - n)).bit_length() - 1
            d = n >> s
            for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
                p = pow(a, d, n)
                if p == 1 or p == n - 1 or a % n == 0:
                    continue
                for _ in range(s):
                    p = (p * p) % n
                    if p == n - 1:
                        break
                else:
                    return False
            return True
        ans = []
        res = [-1,-1]
        mn = float("inf")
        for i in range(left, right+1):
            if is_prime(i):
                ans.append(i)
            if len(ans) == 2:
                if ans[-1] - ans[0] < mn:
                    mn = ans[-1] - ans[0]
                    res = ans[:]
                ans = [i]
        return res
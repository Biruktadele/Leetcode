class Solution:
    def __init__(self):
        self.dec = {}
    
    def fib(self, n: int) -> int:

        if n < 2:
            return n
        elif n in self.dec:
            return self.dec[n]
        self.dec[n] = self.fib(n-1) + self.fib(n-2)
        return self.dec[n]
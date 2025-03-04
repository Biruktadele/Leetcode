class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        l = len(s)
        one = s.count('1')
        ode = ['1']*(one-1) + ["0"]*(l-one) + ['1']
        return "".join(ode)
        
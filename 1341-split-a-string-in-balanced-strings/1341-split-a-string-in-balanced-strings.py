class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        n = 0
        for i in s:
            if i == "L":
                n -= 1
            else:
                n += 1
            if n == 0:
                c += 1
        return c
        
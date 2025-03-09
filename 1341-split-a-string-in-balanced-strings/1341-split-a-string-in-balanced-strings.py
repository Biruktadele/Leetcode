class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cut = 0
        n = 0
        for i in s:
            if i == "L":
                n -= 1
            else:
                n += 1
            if n == 0:
                cut += 1
        return cut
        
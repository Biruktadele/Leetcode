class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        b = False
        count = 0
        for i in d:
            val = d[i]
            count += (d[i]//2) * 2
            if val % 2 == 1:
                b = True
        if b:
            count += 1
        return count 
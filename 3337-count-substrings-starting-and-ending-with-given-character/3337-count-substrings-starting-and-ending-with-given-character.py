class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        s = list(s)
        k = s.count(c)
        return (k*(k+1))//2        
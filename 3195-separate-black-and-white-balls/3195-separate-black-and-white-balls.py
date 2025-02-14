class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        l = 0
        r = 0
        c = 0
        while r < len(s):
            if s[r] == '0':
                if r != l:
                    s[r],s[l] = s[l],s[r]
                    c += r-l
                l += 1
   
            r += 1
        return c
        
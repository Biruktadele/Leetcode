class Solution:
    def makeFancyString(self, s: str) -> str:
        d = {}
        t = ''
        for i in s:
            if i not in d:
                d.clear()
                d[i] = 1
            elif d[i] == 2:
                continue
            else:
                d[i] += 1
            t += i
        return t
        
class Solution:
    def minimumLength(self, s: str) -> int:
        d = defaultdict(int)
        l = len(s)
        for i in s:
            d[i] += 1
            if d[i] == 3:
                d[i] -= 2
                l -= 2
        return l
        


        
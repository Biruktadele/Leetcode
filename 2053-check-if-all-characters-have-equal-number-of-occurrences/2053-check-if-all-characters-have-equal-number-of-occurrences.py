class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        lim = 0
        for i in c:
            if lim == 0:
                prev = i
                lim += 1
                continue
            if c[prev] != c[i]:
                return False
            prev = i
        return True

        
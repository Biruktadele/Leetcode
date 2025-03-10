class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s)
        t = Counter(t)
        return "".join((t - c).keys())
        
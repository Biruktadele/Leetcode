class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        mx = -1
        mn = float("inf")
        for i in c:
            if c[i] % 2:
                mx = max(mx , c[i])
            else:
                mn = min(mn , c[i])
        return mx - mn
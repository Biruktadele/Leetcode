class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors = colors + colors[:k-1]
        c = 0
        l = 0
        r = 1
        diff = 1
        while r < len(colors):
            if colors[r] != colors[r-1]:
                diff += 1
            else:
                diff = 1
            if diff >= k:
                c += 1
            r += 1

        return c
        
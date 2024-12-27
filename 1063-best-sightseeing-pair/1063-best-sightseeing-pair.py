class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        leng = len(values)

        if leng == 2:
            return sum(values)- 1
        l = 0
        r = 2
        mx = values[0]+values[1] - 1

        while r < leng:
            nl = values[l]+values[r] + l - r
            nr = values[r-1]+values[r] - 1

            if nl > nr:
                mx = max(mx,nl)
            else:
                mx = max(mx , nr)
                l = r-1
            r += 1
        return mx



        
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ln = len(heights)
        for i in range(ln):
            l = 0
            r = 1
            while r < ln:
                if heights[l] < heights[r]:
                    heights[l] , heights[r] =  heights[r] , heights[l]
                    names[l], names[r] = names[r], names[l]
                r += 1
                l += 1
        return names
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ln = len(heights)
        for i in range(ln):
            l = i
            r = i
            
            while l < ln:
                
                if heights[l] > heights[r]:
                    heights[l] , heights[r] =  heights[r] , heights[l]
                    names[l], names[r] = names[r], names[l]
            
                l += 1

        return names
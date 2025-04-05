class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxx = 0
        ind = 0
        
        for j , i in enumerate(mat):
            c = i.count(1)
            if c > maxx:
                maxx = c
                ind = j
        return [ind , maxx]
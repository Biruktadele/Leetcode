class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x : x[0])
        x = points[0][1]
        c = 1
        for i in points:
            if x > i[1]:
                x = i[1]
            if x < i[0]:
                x = i[1]
                c += 1
        return c
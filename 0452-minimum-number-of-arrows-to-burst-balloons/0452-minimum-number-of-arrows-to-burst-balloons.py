class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        mn = points[0][1]
        c = 1
        for i in points:
            if i[0] <= mn:
                mn = min(mn , i[1])
            else:
                c += 1
                mn = i[1]
        return c

        
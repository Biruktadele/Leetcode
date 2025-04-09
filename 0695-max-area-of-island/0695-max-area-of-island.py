class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.vist = set()
        def maxarea(grid , r,c):
            row , col = len(grid) , len(grid[0])

            if 0 > r or 0 > c or row <= r or col <= c or grid[r][c] == 0 or (r,c) in self.vist:
                return 0
            self.vist.add((r,c))

            DIRECTIONS_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            s = 0
            for x, y in DIRECTIONS_4:
                s +=  maxarea(grid , r+x,c+y)
            return s + 1
        row , col = len(grid) , len(grid[0])
        maxx = 0
        for i in range(row):
            for j in range(col):
                if (i,j) not in self.vist and grid[i][j] == 1:
                    maxx = max(maxx , maxarea(grid , i,j))
        return maxx

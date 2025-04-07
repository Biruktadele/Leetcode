class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.c = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(grid , r, c , vist):
            row , col = len(grid) , len(grid[0])

            if not (0 <= r < row) or not (0 <= c < col) or grid[r][c] == 0:
                self.c += 1
                return
            vist.add((r,c))
            for x , y in directions:
                new_r = r + x
                new_c = c + y
                if (new_r,new_c) not in vist:
                    dfs(grid , new_r, new_c , vist)
        row , col = len(grid) , len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(grid , i, j , set())
                    return self.c
        return self.c


            

            


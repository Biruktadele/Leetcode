class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.vist = set()
        def dfs(grid , r, c):
            row , col = len(grid) , len(grid[0])

            if not (0 <= r < row) or not (0 <= c < col) or grid[r][c] == "0":
                return 1
            self.vist.add((r,c))
            res = 0
            for x , y in directions:
                new_r = r + x
                new_c = c + y
                if (new_r,new_c) not in self.vist:
                    dfs(grid , new_r, new_c)
            return 1
        row , col = len(grid) , len(grid[0])
        c = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in self.vist:
                    dfs(grid , i, j)
                    c += 1
           
        return c
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        cc = [0]*col
        cr = [0]*row

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    cc[j] += 1
                    cr[i] += 1
        c = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (cc[j] > 1 or cr[i] > 1):
                    c += 1
        return c
                    

        
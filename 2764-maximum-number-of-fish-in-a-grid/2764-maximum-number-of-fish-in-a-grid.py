class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.vist = set()
        row , col = len(grid),len(grid[0])
        def dfs(grid,r,c):
            row,col = len(grid)-1 ,len(grid[0])-1 
            
            q = deque()
            q.append((r,c))
            self.vist.add((r,c))
            s = 0
            while q:
                l = len(q)
                for i in range(l):
                    r,c = q.pop()
                    s += grid[r][c]
                    if (r,c+1) not in self.vist and c < col and  grid[r][c+1]:
                        self.vist.add((r,c+1))
                        q.append((r,c+1))
                    if (r+1,c) not in self.vist and r < row and grid[r+1][c]:
                        self.vist.add((r+1,c))
                        q.append((r+1,c))
                    if (r,c-1) not in self.vist and c > 0 and grid[r][c-1]:
                        self.vist.add((r,c-1))
                        q.append((r,c-1))
                    if (r-1,c) not in self.vist and r > 0 and grid[r-1][c]:
                        self.vist.add((r-1,c))
                        q.append((r-1,c))
            return s

        mx = 0
        for r in range(row):
            for c in range(col):
                if (r,c) not in self.vist and grid[r][c] != 0:
                    mx = max(dfs(grid,r,c),mx)
        return mx

        
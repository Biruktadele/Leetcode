class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.max = 0

        def inbound(x, y, n, m): return 0 <= x < n and 0 <= y < m
        q = deque()
        row , col = len(grid) , len(grid[0])
        c = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    c +=1
        if not q and c:
            return -1
        if not q or not c:
            return 0
        level = 0
        # print(c)
        # print(q)
        while q:
            l = len(q)
            # print(q)
            for i in range(l):
                r , cc = q.popleft()

                for y,x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx = r + x
                    ny = cc + y
                    if inbound(nx , ny ,row ,col) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx , ny))
                        c -= 1
            level += 1
        print(c)
        return level - 1 if c == 0 else -1





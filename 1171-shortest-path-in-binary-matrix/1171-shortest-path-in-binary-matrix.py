class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    
        DIRECTIONS_8 = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
        def inbound(x, y, n, m): return 0 <= x < n and 0 <= y < m
        if grid[0][0] == 1:
            return -1
        q = deque([(0,0)])
        vist = set((0,0))
        row , col = len(grid) , len(grid[0])
        level = 1
        while q:
            l = len(q)
            for i in range(l):
                curr = q.popleft()
                if curr == (row-1, col-1):
                    return level
                for u , v in DIRECTIONS_8:
                    nr = u + curr[0]
                    nc = v + curr[1]
                    if not inbound(nr , nc , row , col) or grid[nr][nc] == 1 or (nr , nc) in vist:
                        continue
                    q.append((nr,nc))
                    vist.add((nr,nc))
            level += 1
        return -1
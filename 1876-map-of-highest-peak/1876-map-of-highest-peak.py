class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        vist = set()
        def inbound(x, y, n, m): return 0 <= x < n and 0 <= y < m

        row , col = len(isWater) , len(isWater[0])
        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    q.append((i,j))
                    vist.add((i,j))
        level = 0
        while q:
            l = len(q)
  
            for i in range(l):
                r , c = q.popleft()
      
                isWater[r][c] = level
                for u ,v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr = u + r
                    nc = v + c
                    if inbound(nr , nc , row,col) and (nr, nc) not in vist:
                        q.append((nr, nc))
                        vist.add((nr, nc))
            level += 1
        return isWater



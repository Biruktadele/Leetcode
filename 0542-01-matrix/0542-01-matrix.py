class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def inbound(x, y, n, m): return 0 <= x < n and 0 <= y < m

        q = deque()
        row , col = len(mat) , len(mat[0])
        vist = set()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i,j))
                    vist.add((i,j))
        level = 1
        while q:
            l = len(q)

            for i in range(l):
                curr = q.popleft()
                r , c = curr

                for x , y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx = x + r
                    ny = y + c
                    if (nx , ny) in vist or not inbound(nx , ny,row,col):
                        continue
               
                    mat[nx][ny] = level
                    vist.add((nx , ny))
                    q.append((nx,ny))

            level += 1
        return mat







class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        def inbound(x, y, n, m): return 0 <= x < n and 0 <= y < m

        row , col = len(moveTime) , len(moveTime[0])
        heap = [[0 , 0 ,0]]
        vist = set((0,0))
        while heap:
            v , x, y = heappop(heap)
            if x == row - 1 and col - 1 == y:
                return v
            for i , j in  [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = i + x
                ny = j + y
                if inbound(nx , ny , row , col) and (nx , ny) not in vist:
                    val = max(moveTime[nx][ny] , v) + 1
                    heappush(heap , [val , nx , ny])
                    vist.add((nx,ny))



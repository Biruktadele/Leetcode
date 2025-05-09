class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def inbound(x, y, n, m): return 0 <= x < n and 0 <= y < m

        # matrix = [[3,4,5],[3,2,6],[2,2,1]]
        row , col = len(matrix) , len(matrix[0])
        heap = []
        for i in range(row):
            for j in range(col):
                heappush(heap , [matrix[i][j] , i , j])
        ans = [[1]*col for _ in range(row)]

        while heap:
            val , i, j= heappop(heap)
            # print(val , i , j)
            for u , v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x , y = i + u , j + v
                if inbound(x , y , row , col) and matrix[x][y] < val:
                    ans[i][j] = max(ans[i][j] , ans[x][y] + 1)
        maxx = 0
        for i in range(row):
            for j in range(col):
                maxx = max(maxx , ans[i][j]) 
        return maxx
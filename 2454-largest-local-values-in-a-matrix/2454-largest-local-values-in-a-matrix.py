class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def maxx(arr , l,t):
            mx = -float("inf")
            for i in range(3):
                for j in range(3):
                    mx = max(mx , arr[i+t][j+l])
            return mx
        ans = []
        row,col = len(grid),len(grid[0])
        for i in range(row-2):
            num = []
            for j in range(col-2):
                mx = maxx(grid,j,i)
                num.append(mx)
            ans.append(num)
        return ans


        
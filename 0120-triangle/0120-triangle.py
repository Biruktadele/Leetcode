class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for  i in range(1,len(triangle)) :
            lng = len(triangle[i])
            for j in range(lng):
                l = max(j-1,0)
                r = min(lng-2, j)
                triangle[i][j] = min(triangle[i-1][l] , triangle[i-1][r]) + triangle[i][j]

        return min(triangle[-1])



        
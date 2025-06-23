class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        r , c = len(mat),len(mat[0])
        
        ans = []
        for i in range(r):
            for j in range(c):
                dic[i+j].append(mat[i][j])
        for i in range(len(dic)):
            if i % 2 == 0:
                dic[i].reverse()
                ans += dic[i]
            else:
                ans += dic[i]
        return ans

        
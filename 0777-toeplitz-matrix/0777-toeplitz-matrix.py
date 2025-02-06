class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d=  {}
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if j-i not in d :
                    d[j-i] = matrix[i][j]
                else:
                    if matrix[i][j] != d[j-i]:
                        return False
        return True

        
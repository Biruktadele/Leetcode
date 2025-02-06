class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if i > 0 and j > 0:
                    if matrix[i-1][j-1] != matrix[i][j]:
                        return False
        return True

        
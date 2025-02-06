class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if len(mat) != len(target) or len(target[0]) != len(mat[0]):
            return False
        r1 = True
        r2 = True
        r3 = True
        r4 = True
        r = len(mat)-1
        c = len(mat[0])-1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != target[i][j]:
                    r1 = False
                if mat[i][j] != target[j][len(mat)-1-i]:
                    r2 = False
                if mat[i][j] != target[r-i][c-j]:
                    r3 = False
                if mat[i][j] != target[r-j][i]:
                    r4 = False

        return r1 or r2 or r3 or r4
        
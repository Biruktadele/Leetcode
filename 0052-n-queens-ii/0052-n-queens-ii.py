class Solution:
    def totalNQueens(self, n: int) -> int:
        def chek(n,i,j):
            if i < 1:
                return True
            for a in range(i):
                if n[a][j] == 'Q':
                    return False
            a,b = i-1,j-1
            while a >= 0 and b >= 0:

                if n[a][b] == 'Q':
                    return False
                a -= 1
                b -= 1
            a,b = i-1,j+1
            while a >= 0 and b < len(n[0]):

                if n[a][b] == 'Q':
                    return False
                a -= 1
                b += 1
            return True
        def dfs(n,i,j,ans):
            r,c = len(n),len(n[0])

            if i == r :

                ans.append(["".join(row[:]) for row in n])
                
                return

            for a in range(c):
                if not chek(n,i,a):
                    continue
                n[i][a] = 'Q'
                dfs(n,i+1,a,ans)
                n[i][a] = '.'




            return ans


        s = []
        for i in range(n):
            s.append(list('.'*n))

        return len(dfs(s,0,0,[]))

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
        def dfs(n,i,j):
            r,c = len(n),len(n[0])

            if i == r :

                self.ans += 1
                
                return

            for a in range(c):
                if not chek(n,i,a):
                    continue
                n[i][a] = 'Q'
                dfs(n,i+1,a)
                n[i][a] = '.'

            return


        s = []
        self.ans = 0
        for i in range(n):
            s.append(list('.'*n))
        dfs(s,0,0)
        return self.ans
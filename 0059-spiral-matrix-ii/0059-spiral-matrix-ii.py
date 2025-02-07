class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num = [[0]*n for i in range(n)]
        vist = set()
        i , j = 0,0
        num[0][0] = 1
        vist.add((0,0))
        c = 1
        r,d,l,u = 1,0,0,0,
        while c < n*n:
            if r:
                if j+1 < n and (i,j+1) not in vist:
                    c += 1
                    num[i][j+1] = c
                    vist.add((i,j+1))
                    
                    j += 1
                else:
                    r= 0
                    d = 1
            elif d:
                if i + 1 < n and (i+1,j) not in vist:
                    c += 1
                    num[i+1][j] = c
                    vist.add((i+1,j))
                    i+= 1
                    # c += 1
                else:
                    d = 0
                    l = 1
            elif l :
                if j-1 >= 0 and (i,j-1) not in vist:
                    c += 1
                    vist.add((i,j-1))
                    num[i][j-1] = c
                    j -= 1
                    # c +=1
                else:
                    l = 0
                    u = 1
            elif u:
                if i-1 >= 0 and (i-1,j) not in vist:
                    c += 1
                    vist.add((i-1,j))
                    num[i-1][j] = c
                    i -= 1
                    # c += 1
                else:
                    u = 0
                    r = 1
        return num


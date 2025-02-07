class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nums = [matrix[0][0]]
        row , col,i,j = len(matrix) , len(matrix[0]),0,0
        vist = set((0,0))
        l ,r,u,d =0,1,0,0
        c = 0
        while c < row*col-1:
            if r:
                if j+1 < col and (i,j+1) not in vist:
                    vist.add((i,j+1))
                    nums.append(matrix[i][j+1])
                    j += 1
                    c += 1
                else:
                    r = 0
                    d = 1
            elif d:
                if i+1 < row and (i+1,j) not in vist:
                    vist.add((i+1,j))
                    nums.append(matrix[i+1][j])
                    i += 1
                    c += 1
                else:
                    l = 1
                    d = 0
            elif l:
                if j-1 >= 0 and (i,j-1) not in vist:
                    vist.add((i,j-1))
                    nums.append(matrix[i][j-1])
                    j -= 1
                    c += 1
                else:
                    u = 1
                    l = 0
            elif u:
                if i-1 > 0 and (i-1,j) not in vist:
                    vist.add((i-1,j))
                    nums.append(matrix[i-1][j])
                    i -= 1
                    c += 1  
                else:
                    u = 0
                    r = 1
    
        return nums
            



        
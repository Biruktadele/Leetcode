class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        direction = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        row = len(img)
        col = len(img[0])
        ans = [[0]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                s = img[i][j]
                c = 1
                for dir in direction:
                    x , y = dir
                    if (x + j) < col and (x + j) >= 0 and (y + i) < row and ( y + i) >= 0:
                        s += img[y+i][x+j]
                        c += 1
                
                ans[i][j] = s//c
                
        return ans


                    

                    

    

       
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        size = 0
        row , col = len(isConnected) ,len(isConnected)
        parent = [i for i in range(row+1)]
        rank = [i for i in range(row+1)]
        comp = row
        def find(x):
            if x == parent[x]:
                return x
            return find(parent[x])
        def uninon(x , y):
            nonlocal comp
            rx = find(x)
            ry = find(y)

            if rx == ry:
                return 
            if rank[rx] > rank[ry]:
                parent[ry] = rx
 
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
          
            else:
                parent[rx] = ry
                rank[ry] += 1
            comp -= 1
        for i in range(row):
            for j in range(col):
                if isConnected[i][j] == 1:
                    uninon(i , j)
        return comp


        

      

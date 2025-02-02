class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        if grid[0][0] != 0:
            return -1
        q.append((0,0))
        vist =set()
        vist.add((0,0))
        row ,col = len(grid)-1 , len(grid[0])-1
        if row == 0 and col == 0:
            return 1
        count = 1

        while q:
            way = False
            l = len(q)
            
            for i in range(l):
                r , c = q.popleft()
                if r > 0 and grid[r-1][c] == 0 and (r-1,c) not in vist:
                    vist.add((r-1,c))
                    q.append((r-1,c))
                    way = True
                if r > 0 and c > 0 and grid[r-1][c-1] == 0 and (r-1,c-1) not in vist:
                    vist.add((r-1,c-1))
                    q.append((r-1,c-1))
                    way = True
                if c > 0 and grid[r][c-1] == 0 and (r,c-1) not in vist:
                    vist.add((r,c-1))
                    q.append((r,c-1))
                    way = True
                if r < row and c > 0 and grid[r+1][c-1] == 0 and (r+1,c-1) not in vist:
                    vist.add((r+1,c-1))
                    q.append((r+1,c-1))
                    way = True
                if r < row and grid[r+1][c] == 0 and (r+1,c) not in vist:
                    vist.add((r+1,c))
                    q.append((r+1,c))
                    way = True
                if r < row and c < col and grid[r+1][c+1] == 0 and (r+1,c+1) not in vist:
                    vist.add((r+1,c+1))
                    q.append((r+1,c+1))
                    print("yes")
                    way = True
                if r > 0 and c < col and grid[r-1][c+1] == 0 and (r-1,c+1) not in vist:
                    vist.add((r-1,c+1))
                    q.append((r-1,c+1))
                    way = True
                if c < col and grid[r][c+1] == 0 and (r,c+1) not in vist:
                    vist.add((r,c+1))
                    q.append((r,c+1))
                    way = True
            count += 1
            if (row ,col) in vist:
                return count
            if not way:
                return -1    
            
        return count


        
        
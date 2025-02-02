class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island_set = set()
        def find_island_dfs(r,c):
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or grid[r][c] == 0:
                return 
            
            island_set.add((r,c))
            grid[r][c] = 0
            find_island_dfs(r+1,c)
            find_island_dfs(r-1, c)
            find_island_dfs(r, c+1)
            find_island_dfs(r, c-1)
        
        def shortest_path_bfs():
            q = deque([[r, c] for r,c in island_set])
            steps = [(1,0),(0,1), (-1,0), (0, -1)]
            level = 0
            while q:
                n = len(q)
                for _ in range(n):
                    x,y = q.popleft()

                    for dx,dy in steps:
                        nx,ny = x + dx, y+dy

                        if nx < 0 or ny < 0 or nx > rows - 1 or ny > cols - 1 or (nx,ny) in island_set:
                            continue
                        if grid[nx][ny] == 1:
                            return level
                        island_set.add((nx,ny))
                        q.append([nx,ny])
                level += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    find_island_dfs(row, col)
                    return shortest_path_bfs()
        return -1
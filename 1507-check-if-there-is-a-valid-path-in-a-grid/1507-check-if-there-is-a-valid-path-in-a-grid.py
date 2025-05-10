class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        m, n = len(grid), len(grid[0])
        
        # Directions and connections
        dirs = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)]       # right, up
        }
        
        # Reverse mapping for incoming connections
        reverse = {
            (0, -1): (0, 1),   # left <-> right
            (0, 1): (0, -1),
            (1, 0): (-1, 0),   # down <-> up
            (-1, 0): (1, 0)
        }
        
        queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while queue:
            x, y = queue.popleft()
            if (x, y) == (m - 1, n - 1):
                return True
            
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if reverse[(dx, dy)] in dirs[grid[nx][ny]]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        
        return False

        
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = [False] * n
        min_heap = [(0, 0)]  # (cost, point_index)
        total_cost = 0
        count = 0

        while count < n:
            cost, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += cost
            count += 1

            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (dist, v))
        
        return total_cost
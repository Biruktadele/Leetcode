class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))

        def dijkstra(start, graph):
            dist = {i : float('inf') for i in range(1,n+1)}
            dist[start] = 0
            pq = [(0, start)]

            while pq:
                dis, node = heapq.heappop(pq)

                if dis > dist[node]:
                    continue
                
                for nei, w in graph[node]:
                    new_dis = dis + w
                    if new_dis < dist[nei]:
                        dist[nei] = new_dis
                        heapq.heappush(pq, (new_dis, nei))
            return dist

        shortest_path = dijkstra(n, graph)
        count = 0
        MOD = 10**9 + 7
        memo = {}

        def dfs(node):
            if node == n:
                return 1

            if node in memo:
                return memo[node]

            cnt = 0
            for nei, _ in graph[node]:
                if shortest_path[node] > shortest_path[nei]:
                    cnt = (cnt + dfs(nei)) % MOD

            memo[node] = cnt
            return memo[node]

        return dfs(1)
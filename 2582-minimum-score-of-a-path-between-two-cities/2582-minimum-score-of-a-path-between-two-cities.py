class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        w = defaultdict(lambda : float("inf"))
        for u,v,wg in roads:
            graph[u].append((v,wg))
            graph[v].append((u,wg))
            w[u] = min(w[u], wg)
            w[v] = min(w[v], wg)

        mn= float("inf")
        q = deque([1])
        visited = set([1])
        while q:
            node = q.popleft()
            for v,wg in graph[node]:
                if v not in visited:
                    mn = min(mn,wg)
                    q.append(v)
                    visited.add(v)
        for i in visited:
            mn = min(mn , w[i])
        return mn
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph1 = defaultdict(list)
        indgree = [0] * len(graph)
        for i in range(len(graph)):
            for j in graph[i]:
                graph1[j].append(i)
                indgree[i] += 1
        # print(graph1)
        q = deque()
        # print(indgree)
        
        for j , i in enumerate(indgree):
            if indgree[j] == 0:
                q.append(j)
        ans = []
        # print(q)
        while q:
            curr = q.popleft()
            ans.append(curr)
            for u in graph1[curr]:
                indgree[u] -= 1
                if indgree[u] == 0:
                    q.append(u)
        return sorted(ans)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ord = []
        graph = defaultdict(list)
        indegree = [0]*  numCourses
        q = deque()

        for u , v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            ord.append(curr)

            for u in graph[curr]:
                indegree[u]-= 1
                if indegree[u] == 0:
                    q.append(u)
        if len(ord) != numCourses:
            return []
        return ord
                
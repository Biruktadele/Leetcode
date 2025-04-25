class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            in_degree[node] -= 1

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if len(order) == numCourses:
            return True
        return False
        
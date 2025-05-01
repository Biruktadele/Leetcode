class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        l = len(graph)
        safe = {}
        
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False

            for neg in graph[i]:
                if not dfs(neg):
                    return False
            safe[i] = True
            return safe[i]




        res = []
        for i in range(l):
            if dfs(i):
                res.append(i)
        return res
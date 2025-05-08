class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for fro,to in redEdges:
            adj[fro].append((to,0))
        for fro,to in blueEdges:
            adj[fro].append((to,1))
        pathLength = [float('inf')]*n
        pathLength[0] = 0
        q = deque()
        q.append((0,-1,0))
        visited = set()
        visited.add((0,-1))
        cost = 0
        while q:
            node, prevColor,prevCost = q.popleft()
            pathLength[node] = min(pathLength[node],prevCost)
            for to,col in adj[node]:
                if col!=prevColor and (to,col) not in visited:
                    q.append((to,col,prevCost+1))
                    visited.add((to,col))
        pathLength = [x if x!=float('inf') else -1 for x in pathLength]
        return pathLength
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjlist = defaultdict(list)
        for u ,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        def dfs(adjlist , val , vist):
            if val == destination:
                return True
            if val in vist:
                return False
            vist.add(val)
            for u in adjlist[val]:
                if u not in vist:
                    if dfs(adjlist , u,vist):
                        return True
            return False
        
        return dfs(adjlist , source,set())
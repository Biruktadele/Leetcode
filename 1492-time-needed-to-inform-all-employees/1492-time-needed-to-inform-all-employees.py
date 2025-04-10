class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        
        for i in range(len(manager)):
            if manager[i] == -1:
                continue
            adj[manager[i]].append(i)
        def dfs(n):
            if not adj[n]:
                return informTime[n]
            res = 0
            for u in adj[n]:
                res = max(res , dfs(u))
            return informTime[n] + res
            
        return dfs(headID)
            

        
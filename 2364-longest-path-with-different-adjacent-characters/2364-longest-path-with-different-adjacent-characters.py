class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
   

        for i in range(len(s)):
            if parent[i] == -1:
                continue
            graph[parent[i]].append(i)
        maxx = 0
        def dfs(root , s):
            nonlocal maxx
            if not graph[root]:
                maxx = max(maxx , 1)
                return 1 , s[root]
            ans  = 0
            path = []
            for child in graph[root]:
                val , char = dfs(child , s)
                if char != s[root]:
                    path.append(val)
                    if len(path)  > 2:
                        path.sort(reverse = True)
                        path.pop()
                    maxx = max(maxx , sum(path) + 1)
                    ans = max(ans , val)
            maxx = max(maxx , ans + 1)
            return ans + 1 , s[root]
        dfs(0 , s)
        return maxx
        
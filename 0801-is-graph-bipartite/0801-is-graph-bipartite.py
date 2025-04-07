class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = [-1] * len(graph)

        def dfs(graph , color , val , c ):

            if color[val] != -1:
                return color[val] != c
            color[val] = c
            res = True

            for i in graph[val]:
                if color[i] == -1:
                    res = res and dfs(graph , color , i , 1 - c)
                else:
                    res = res and color[i] != c
            return res
        res = True
        for i in range(len(graph)):
            if color[i] == -1:
                res = res and dfs(graph , color , i , 0)
        
        return res


            
        

        

        
        
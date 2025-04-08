class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1] * (n+1)
        graph = defaultdict(list)
        for u , v in dislikes:
            graph[u].append(v)
            graph[v].append(u)


        def group(graph , color , val , c):
            if color[val] != -1:
                return color[val] != c
            color[val] = c
            res = True
            for u in graph[val]:
              
                if color[u] != -1:
                    res &= color[u] != c
                else:
                    res &= group(graph , color , u , 1-c)
            return res
        res = True
        for i in range(1,n+1):
            if color[i] == -1:
                res &= group(graph , color , i , 0)

        return res



        
            


        
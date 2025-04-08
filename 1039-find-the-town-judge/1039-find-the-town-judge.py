class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        color = [0]*(n+1)
        adjlist = defaultdict(list)
        if trust == []:
            if n < 2:
                return 1
            else:
                return -1
        for u , v in trust:
            adjlist[u].append(v)
            color[v] += 1

        mx = color.index(max(color))
        if adjlist[mx] or color[mx] != n-1:
            return -1
        return mx

        
        
        
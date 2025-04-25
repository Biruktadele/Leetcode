class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)
        for u , v in prerequisites:
            graph[v].append(u)

        def dfs(node , targe , vist):
            if node in vist:
                return False
            if node == targe:
                return True
            vist.add(node)
            res = False
            for u in graph[node]:
                if dfs(u , targe , vist):
                    return True
            return res
        ans = []
        for i in queries:
            ans.append(dfs(i[1] , i[0] , set()))
        return ans




        
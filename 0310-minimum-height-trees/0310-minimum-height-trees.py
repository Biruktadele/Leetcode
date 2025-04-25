class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        vist = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        max_path = 0
        maxx_path = [[]]
        def longest_path(node, parent , path):
            nonlocal max_path
            if node in vist:
                return
            vist.add(node)
            path.append(node)
            if len(path) >= max_path:
                max_path = len(path)
                maxx_path.clear()
                maxx_path.append(path.copy())
            for neighbor in graph[node]:
                if neighbor != parent:
                    longest_path(neighbor, node, path)
            path.pop()
            vist.remove(node)
        longest_path(0, -1, [])
        num = maxx_path[0][-1]
        max_path = 0
        maxx_path = [[]]
        longest_path(num, -1, [])
        if max_path%2:
            return [maxx_path[0][max_path//2]]
        else:
            mid = (max_path- 1) // 2
            return maxx_path[0][mid:mid+2]
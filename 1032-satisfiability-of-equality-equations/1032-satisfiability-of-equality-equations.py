class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        arr = defaultdict(str)
        rank = defaultdict(int)
        

        def find(x):
            while arr[x]:
                x = arr[x]
            return x
        def union(x , y):
            px = find(x)
            py = find(y)
            if px == py:
                return 
            if rank[px] > rank[py]:
                arr[py] = px
            elif rank[px] < rank[py]:
                arr[px] = py
            else:
                arr[px] = py
                rank[py] += 1
        for i in equations:
            if i[1:3] == "==":
                union(i[0] , i[-1])
        
        for i in equations:
            if i[1:3] == "!=" :
                # print(i[0] , i[-1])
                print(find(i[0]), find(i[-1]) )
                if find(i[0]) == find(i[-1]):
                    return False
        return True
                

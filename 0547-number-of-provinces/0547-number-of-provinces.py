class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        con = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if j != i and isConnected[i][j] == 1:
                    con[i].append(j)
        self.vist = set()

        def comp(v):
            if not con[v] or v in self.vist:
                return
            self.vist.add(v)
            for u in con[v]:
                comp(u)
        notconnecteds = 0
        for i in range(len(isConnected)):
            if i not in self.vist:
                comp(i)
                notconnecteds += 1
        return notconnecteds
      

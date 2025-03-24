class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = "abc"

        self.count = 0

        def dfs(s,n,k,path):
           
            if len(path) == n:
                self.count += 1
                if self.count == k:
                    ans.append("".join(path[:]))
                return 
            for i in range(3):
                if not path or path[-1] != s[i]:
                    path.append(s[i])
                    dfs(s,n,k,path)
                    path.pop()
                    if len(ans) > 0:
                        return
        s = "abc"
        ans = []
        dfs(s,n,k,[])
        return ans[0] if ans else ""
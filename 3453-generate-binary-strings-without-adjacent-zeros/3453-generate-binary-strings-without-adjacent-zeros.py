class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def valid(num):
            res = []
            for i in num:
                for j in range(1 , len(i)):
                    if i[j-1:j+1] == "00":
                        break

                else:
                    res.append(i)
            return res

        def dfs(n , path):
            if len(path) == n:
                ans.append("".join(path))
                return

            path.append('0')
            dfs(n , path)
            path[-1] = '1'
            dfs(n , path)
            path.pop()
        dfs(n , [])

        return valid(ans)

        
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        s = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        l = len(digits)
        ans = []

        def dfs(digit,i,path,c,s):
            if len(path) == len(digit):
                ans.append(''.join(path))
                return
            x = int(digit[c])-2
            l = len(s[x])
            for i in range(l):
                path.append(s[x][i])
                dfs(digit,i,path,c+1,s)
                path.pop()
            return
        dfs(digits,0,[],0,s)
        if ans[0] == '':
            ans.pop()
        return ans
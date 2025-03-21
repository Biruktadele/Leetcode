class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def dfs(num , s , f , path):
           
            if f >= len(s):
                if num == sum(path):
                    self.ans = True
                return 
            
            for i in range(f, len(s)):
                path.append(int(s[f:i+1]))
                dfs(num , s , i+1 , path)
                path.pop()
        summ = 0
        for i in range(1,n+1):
            s = str(i**2)
            self.ans = False
            dfs(i , s , 0 , [])
            if self.ans:
                summ += i**2
        return summ
        

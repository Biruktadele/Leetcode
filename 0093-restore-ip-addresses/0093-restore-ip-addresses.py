class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def valid(string):
            ls = string.split(".")
            for s in ls:
                if not s or int(s)>255 or int(s)<0 or (len(s)>1
                 and s[0]=='0'):
                    return False
            return True
        def backtrack(i,n,curr):
            if n==3:
                if valid(curr):
                    res.append(curr)
                return
            
            for idx in range(i+1,len(curr)):
                temp = curr[:idx]+"."+curr[idx:]
                backtrack(idx,n+1,temp)
            return 

        
        backtrack(0,0,s)
        return res
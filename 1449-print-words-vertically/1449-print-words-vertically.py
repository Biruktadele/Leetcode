class Solution:
    def printVertically(self, s: str) -> List[str]:
        mx = 1
        s = s.split()
        for i in s:
            mx = max(mx , len(i) )
        ans = []
        for j in range(mx):
            temp = ""
            st = ""

            for i in range(len(s)):
                if j < len(s[i]):
                    temp += st + s[i][j]
                    st = ""
                else:
                    st += " "
            ans.append(temp)
        return ans
        
                
        
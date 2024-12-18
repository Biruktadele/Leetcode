class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def pallendrom(s):
            Mx = 1
            i  = 1
            while i <= len(s)//2 + 1:
                rev = s[i+1:2*i+1]
                rev.reverse()

                if s[0:i] == rev:
                    Mx = 2*i + 1
                i += 1
            mx = 0
            i=0
            while len(s) > 1 and i < len(s)//2 + 1:
                norm = s[0:i]
                rev = s[i:i*2]
                rev.reverse()
                if norm == rev:
                    mx = (i)*2
                i += 1
            return max(mx,Mx)
        s = list(s)
        x = pallendrom(s)
        newstr = s[x::]
        newstr.reverse()
        s = newstr+s
        return ''.join(s)
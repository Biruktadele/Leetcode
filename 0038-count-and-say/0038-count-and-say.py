class Solution:
    def countAndSay(self, n: int) -> str:
        def sey(s):
            d = {}
            ch = s[0]
            c = 1
            st = ""
            for i in range(1,len(s)):
                if s[i] == ch:
                    c+= 1
                else:
                    st += str(c)+ch
                    ch = s[i]
                    c = 1
            st += str(c)+ch
            return st
        i = 1
        s = '1'
        if n == 1:
            return '1'
        while i < n:
            s = sey(s)
            i += 1
        return s
            
        
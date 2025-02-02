class Solution:
    def maskPII(self, s: str) -> str:
        def isphone(c):
            s = ""

            count = 0
            j = 0
            for i in range(len(c)-1,-1,-1):
                if c[i].isdigit():
                    s = c[i] + s
                    count += 1
            s = s[-4::]
            s = "***-"*2 + s
            d = count - 10
            if d > 0:
                s = "+"+"*"*d+"-"+s
            return s

        def isemail(em):
            em = em.lower()

            for i in range(len(em)):
                if em[i] == '@':
                    break
            s = em[0]+ "*"*5 +em[i-1:]
            return s
        if s[0].isalpha():
            return isemail(s)
        return isphone(s)

        

        
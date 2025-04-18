class Solution:
    def countAndSay(self, n: int) -> str:
        def sey(s):
            t = s[0]
            c = 1
            ans = []
            for i in s[1::]:
                if i == t:
                    c += 1
                else:
                    ans.append(str(c))
                    ans.append(t)
                    t = i
                    c = 1
            ans.append(str(c))
            ans.append(t)
            return "".join(ans)
        def count(n):
            if n == 1:
                return "1"
            return sey(count(n-1))
        return count(n)
            

        
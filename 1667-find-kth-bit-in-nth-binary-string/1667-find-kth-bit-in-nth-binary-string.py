class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def inverter(s):
            ans = []
            for i in s:
                x = "0" if i == "1" else "1"
                ans.append(x)
            ans.reverse()
            return "".join(ans)
        def bins(n,c):
            if c == n:
                return "0"
            s = bins(n,c+1)
            y = inverter(s)

            return s + "1" + y
    
        return bins(n,0)[k-1]


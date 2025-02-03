class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        i = columnNumber
        while i > 0:
            temp = (i-1)%26
            ans += chr(65 + temp)
            i = (i-1)//26
        ans = list(ans)
        ans.reverse()
        return "".join(ans)
            


        
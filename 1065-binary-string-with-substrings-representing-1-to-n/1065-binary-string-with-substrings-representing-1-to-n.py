class Solution:
    def queryString(self, s: str, n: int) -> bool:
        flag=True
        for i in range(1,n+1):
            if flag==False:return False
            if str(bin(i))[2:] in s:flag=True
            else:return False
        return flag
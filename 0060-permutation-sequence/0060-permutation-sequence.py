class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = [i for i in range(1,n+1)]
        prifx = [1]
        for i in range(1,n):
            prifx.append(i * prifx[i-1])
        # print(prifx)
        # print(num)
        rim = k -1
        s = ''
        for i in range(1,n):
            div = rim // prifx[-i]
            rim = rim % prifx[-i]

            s += str(num[div])
            num.pop(div)
        return s + str(num[0])
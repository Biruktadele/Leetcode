class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        d = {}

        for i in banned:
            if i not in d:
                d[i] = 1
        s = 0
        c = 0
        ans =[]
        for i in range(1,n+1):
            if i not in d and s + i <= maxSum:
                s += i
                c += 1
                ans.append(i)
        # print(banned[0:7])
        # print(ans)
        return c



        


        
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def subset(n , i ,c):
            # global ans
            # print(path)
            if c == len(n):
                # print(path)
                return ans.append(path[:])

            path.append(n[i])
            subset(n,i+1,c+1)
            path.pop()
            subset(n,i+1,c+1)

            return
        # n = [1,1,2,2]
        subset(nums,0,0)
        for i in range(len(ans)):
            ans[i].sort()
        ans.sort()
        l = 1
        r = len(ans)-1


        # print(ans)
        s = [ans[0]]
        while l < len(ans):
            if ans[l] == ans[l-1]:
                l += 1
                continue
            s.append(ans[l])
            l += 1
        return s

   
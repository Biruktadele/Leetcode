class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(num , level ,path):
            if level >= len(num):
                if path not in ans:
                    ans.append(path[:])
                return

            for i in range(level , len(num)):
                path.append(num[i])
                dfs(num , i + 1 ,path)
                path.pop()
                dfs(num , i + 1 ,path)
        dfs(nums , 0 ,[])
        return ans


        
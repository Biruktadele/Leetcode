class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def dfs(num , i , vist , path):
            if len(path) == len(num):
                ans.append(path[:])
                return
            
            for i in range(len(num)):
                if i in vist:
                    continue
                vist.add(i)
                path.append(num[i])
                dfs(num , i , vist , path)
                vist.remove(i)
                path.pop()
        dfs(nums , 0 , set() , [])
        return ans
        
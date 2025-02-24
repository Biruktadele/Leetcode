class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    
        ans = set()           
            

        def dfs(nums , f  , path ):

            col = len(nums)
            if len(path) >= 2:
                ans.add(tuple(path))  

            for i in range(f, col):
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    dfs(nums, i +1, path)
                    path.pop()
        
        dfs(nums , 0  , [] )
        return list(ans)
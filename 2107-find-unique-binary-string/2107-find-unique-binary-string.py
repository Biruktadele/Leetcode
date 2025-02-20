class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []

        def dfs(k , path , vist):
            if  len(path) == k:
                if "".join(path) not in vist:
                    ans.append(path[:])
                    return ans
                return 
            for i in range(2):
                s = str(i)
                
                path.append(s)
                dfs(k,path,vist)
                path.pop()
                if len(ans) == 1:
                    return 
        vist = set(nums)
        print(vist)
        k = len(nums)
        dfs(k, [] , vist)
        return "".join(ans[0])
        
class Solution:
    def isAdditiveNumber(self, nums: str) -> bool:

        def dfs(num , path , i):
            
            res = False
            if len(path) >= 3:
                if (int(path[-1]) != int(path[-2]) + int(path[-3])) or len(str(int(path[-1]))) != len(path[-1]) or len(str(int(path[-1-1]))) != len(path[-1-1]) or len(str(int(path[-1-2]))) != len(path[-1-2]):
                    return res
            if i >= len(nums):
                return True if len(path) > 2 else False
            for j in range(i , len(num)):
                path.append(num[i:j+1])
                res = res or dfs(num , path , j+1)
                path.pop()
            return res

        return dfs(nums , [] , 0)


        
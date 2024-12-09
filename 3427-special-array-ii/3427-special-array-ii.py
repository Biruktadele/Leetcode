class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefx = [0]
        for i in range(1,len(nums)):
            c = 0
            if nums[i-1]%2 == nums[i]%2:
                c = 1
            prefx.append(prefx[-1]+c)
        ans = []
        for i in queries:
            ans.append(prefx[i[0]] == prefx[i[1]])    
        return ans
                 


        
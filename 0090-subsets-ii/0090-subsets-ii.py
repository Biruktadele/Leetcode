class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(index,curr):
            if curr not in result:
                result.append(curr[:])
            for i in range(index,len(nums)):
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()
        
        result=[]
        backtrack(0,[])
        return result

        
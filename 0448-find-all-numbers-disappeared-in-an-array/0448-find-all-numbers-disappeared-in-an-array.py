class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums) + 1
        nums= set(nums)
        
        ans = []
        print(n)
        for i in range(1,n):
            if i not in nums:
                ans.append(i)
        return ans

        
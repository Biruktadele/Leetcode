class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = len(nums)
        arr = []
        c = 0

        for i in range(l-1):
            if nums[i] == nums[i+1]:
                nums[i] = 2 * nums[i]
                nums[i+1] = 0
            if nums[i] == 0:
                c += 1 
            
        for i in nums:
            if i:
                arr.append(i)

            
                
        return arr + [0]*(l - len(arr))
            
            


        
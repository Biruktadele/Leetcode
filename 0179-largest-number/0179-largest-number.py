class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i , n in enumerate(nums):
            nums[i] = str(n)
        def comp(n1,n2):
            if n1+n2>n2+n1:
                return -1
            else:
                return 1
        num = sorted(nums , key = cmp_to_key(comp))
        return str(int("".join(num)))  


        
    
        
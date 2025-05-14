class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        s= 0
        for i in nums:
            s ^= i
        n = s & -s
        a = b= 0
        for i in nums:
            if n & i:
                a ^= i
            else:
                b^= i
        return [a,b]


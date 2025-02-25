class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        
        odd = 0
        even = 0
        pre = 0
        c = 0
        mod = 10**9 + 7
        for i in arr:
            pre += i
            if pre % 2:
                c += even + 1
                odd += 1
            else:
                c += odd
                even += 1
        return c% mod
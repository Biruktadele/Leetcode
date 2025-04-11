class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c = 0
        for i in range(low , high+1):
     
            s = [int(i) for i in str(i)]
            if len(s) % 2:
                continue
            mid = len(s)//2
            if sum(s[:mid]) == sum(s[mid:]):

                c += 1
        return c

        
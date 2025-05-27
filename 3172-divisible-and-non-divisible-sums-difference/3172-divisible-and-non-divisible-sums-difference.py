class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s1 = 0
        s2 =0
        for i in range(1 , n+1):
            if i % m:
                s2 += i
            else:
                s1 += i
        return  s2 -s1
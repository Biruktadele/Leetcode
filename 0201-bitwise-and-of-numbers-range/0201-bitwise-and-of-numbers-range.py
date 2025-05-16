class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        res = right
        n = res.bit_length()
        j = 0
        while j < n:

            if res & (1<<j) and left & (1 << j):
                if res & ~(1 << j) >= left:
                    res &= ~(1 << j)
            else:
                res &= ~(1 << j)
            j += 1
        return res
            
        
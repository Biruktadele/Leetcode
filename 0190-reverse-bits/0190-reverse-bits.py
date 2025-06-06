class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):  # place bits in res from right to left
            bit = (n >> i) & 1  # right shift to rightmost pos and isolate bit
            res |= (bit << (31 - i))  # leftshift isolated bit into pos
        return res
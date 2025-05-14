class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt = num2.bit_count()
        res = 0

        for i in range(31, -1, -1):
            if (num1 >> i) & 1:
                res |= (1 << i)
                cnt -= 1
                if cnt == 0:
                    break

        if cnt > 0:
            for i in range(32):
                if ((res >> i) & 1) == 0:
                    res |= (1 << i)
                    cnt -= 1
                    if cnt == 0:
                        break

        return res



        
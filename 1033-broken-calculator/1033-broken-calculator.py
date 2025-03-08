class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        c = 0
        while target:
            if target == startValue:
                return c
            if target > startValue:
                if target % 2:
                    target = (target+1)//2
                    c += 1
                else:
                    target = target//2
                c += 1
            else:
                c += (startValue - target )
                return c
        
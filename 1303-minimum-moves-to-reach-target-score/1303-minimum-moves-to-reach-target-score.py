class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        minn_opp = 0
        c = 0
        while target > 1 :
            if target % 2 == 0 and maxDoubles:
                target =  target // 2
                c += 1
                maxDoubles -= 1
            else:
                if not  maxDoubles:
                    c += target - 1
                    break

                c += 1
                target -= 1
        return c

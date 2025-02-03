class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set()

        for i in ranges:
            h = {j for j in range(i[0],i[1]+1)}
            s.update(h)
        for j in range(left, right+1):
            if j not in s:
                return False
                break
        else:
            return True
        
class Solution:
    def coloredCells(self, n: int) -> int:
     
        n = ((n-1) * (n))//2
        return 1 +4 *n

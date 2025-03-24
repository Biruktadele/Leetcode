class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0,1:1,2:1}
        def tribonachi(n):
            if n in memo:
                return memo[n]
            memo[n] = tribonachi(n-1) + tribonachi(n-2) + tribonachi(n-3)
            return memo[n]
        return tribonachi(n)

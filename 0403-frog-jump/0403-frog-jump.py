class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if stones[1] - stones[0] > 1:
            return False

        stone = defaultdict(int)
        for idx, unit in enumerate(stones):
            stone[unit] = idx

        @cache
        def dp(unit: int, k: int) -> bool:

            if unit not in stone or unit < 0:
                return False

            if stone[unit] == len(stones) - 1:
                return True

            ans = False
            for jump in (k-1, k, k+1):
                if jump > 0:
                    ans = ans or dp(unit + jump, jump)

            return ans
            
        return dp(stones[1], 1)
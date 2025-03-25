class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(piles , speed):
            hour = 0
            for i in piles:
                hour += math.ceil(i / speed)
            return hour
        l = 1
        r = max(piles)

        while l < r:
            mid = (l+r)//2

            if can_eat(piles , mid) <= h:
                r = mid
            else:
                l = mid + 1
        return l
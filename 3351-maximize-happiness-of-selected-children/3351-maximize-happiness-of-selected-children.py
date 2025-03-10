class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        i = 0
        res = 0
        while i < k:
            res += max(0, (happiness[i] - i))
            i += 1
        return res


        
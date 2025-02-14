class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        vist = defaultdict(int)
        c = 0
        mx = 0
        for r in range(len(fruits)):
            vist[fruits[r]] += 1
            c = len(vist)

            while c > 2:
                vist[fruits[l]] -= 1
                if vist[fruits[l]] == 0:
                    vist.pop(fruits[l])
                l += 1
                c = len(vist)
            mx = max(mx ,r-l + 1)
        return mx
            

        
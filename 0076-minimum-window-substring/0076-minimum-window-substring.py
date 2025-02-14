class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        target = Counter(t)
        def cheak(wind , target):
            if len(target - wind):
                return False
            else:
                return True
        mx = []
        wind = Counter()
        for r in range(len(s)):
            wind[s[r]] += 1

            while cheak(wind , target):
                if mx == [] or mx[1] - mx[0] + 1 > r - l +1:
                    mx = [l,r]
                wind[s[l]] -= 1
                l += 1
            
        return s[mx[0]:mx[1]+1] if mx else ""




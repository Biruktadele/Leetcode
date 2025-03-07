class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = math.ceil(len(arr) / 2)

        c = Counter(arr)
        num = sorted(list(c.values()), reverse = True)

        wind = 0
        c = 0
        minn = float(inf)
        l = 0

        for j,i in enumerate(num):
            wind += i
            c += 1
            while wind >= half:
                minn = min(minn,c)
                wind -= num[l]
                l += 1
                c -= 1
        return minn

        
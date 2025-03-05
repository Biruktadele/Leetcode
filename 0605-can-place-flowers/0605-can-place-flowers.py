class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0]+flowerbed+[0]
        one = sum(flowerbed[0:2])
        l = 0
        r = 2
        c = 0
        while r < len(flowerbed):
            one += flowerbed[r]

            if one == 0:
                c += 1
                l = r
                one += sum(flowerbed[r:r+2])
                r += 2
                continue
            one -= flowerbed[l]
            l += 1
            r += 1
        return c >= n

        
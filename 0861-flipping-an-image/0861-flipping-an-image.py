class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            l = 0
            r = len(i)-1
            while l <= r:
                if l == r:
                    print(l)
                    i[l] = int(not i[l])
                    l+=1
                    continue
                i[l],i[r] = int(not i[r]), int(not i[l])
                l += 1
                r -= 1
        return image
        
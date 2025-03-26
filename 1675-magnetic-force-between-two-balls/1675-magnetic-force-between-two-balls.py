class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def distribute(pos , force , m):

            c = 1
            ind = 0
            for i in range(1, len(pos)):
                if abs (pos[i] - pos[ind]) >= force:
                    c += 1
                    ind = i

            return c >= m
            
        position.sort()
        best = 1
        l = 1
        r = max(position)

        while l <= r:
            mid = l + (r-l)//2

            if distribute(position ,mid , m):
                l = mid + 1
                best = mid
            else:
                r = mid - 1
        return best
class Solution:
    def countSubarrays(self, num: List[int], mink: int, maxk: int) -> int:

        s = 0
        minn = -1
        maxx= -1
        limit = -1

        for i in range(len(num)):
            if num[i] > maxk or num[i] < mink:
                limit = i
            if num[i] == mink:
                minn = i
            if num[i] == maxk:
                maxx = i
            s += max(0, min(minn , maxx) - limit)
        return s 
        
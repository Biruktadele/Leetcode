class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        tx = tops[0]
        bx = bottoms[0]
        ct = 0
        cb = 0
        bt = 0
        bb = 0
        n = len(tops)
        for i in range(len(tops)):
            if tx != tops[i] and tx != bottoms[i]:
                ct = float("inf")
            elif tx != tops[i]:
                ct += 1
            if tx != tops[i] and tx != bottoms[i]:
                cb = float("inf")
            elif tx != bottoms[i]:
                cb += 1
            if bx != tops[i] and bx != bottoms[i]:
                bt = float("inf")
            elif bx != tops[i]:
                bt += 1
            if bx != tops[i] and bx != bottoms[i]:
                bb = float("inf")
            elif bx != bottoms[i]:
                bb += 1
        minn = min(ct , cb , bt , bb)
        return minn if minn != float("inf") else -1
            
                

            

        
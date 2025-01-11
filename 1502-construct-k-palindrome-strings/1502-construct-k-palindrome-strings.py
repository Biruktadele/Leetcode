class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        sl = len(s)
        if k > sl:
            return False
        d = Counter(s)
        b = True
        c = 0
        for i in d:
            if d[i] %2 == 0:
                if b:
                    c += 1
                    b = False
            else:
                c += 1
        if not b:
            return c-1<=k or c <= k
        return c <= k
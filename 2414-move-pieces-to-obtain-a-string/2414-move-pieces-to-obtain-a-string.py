class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # from collections import defaultdict
        st ,ta= defaultdict(int),defaultdict(int)

        l = r= 0
        sz = len(start)

        for i in range(sz):
            s1 = start[i]
            s2 = target[i]
            st[s1] += 1
            ta[s2] += 1

        if st['L'] != ta['L'] or st['R'] != ta['R'] or st['_'] != ta['_']:
            return False
        while l < sz and r < sz:
            s1 = start[l]
            s2 = target[r]
            while s1 == '_' and l < sz-1:
                l += 1
                s1 = start[l]
            while s2 == '_' and r < sz-1:
                # print(s1 ,s2)
                r += 1
                s2 = target[r]
            if s1 != s2 :
                return False
            elif s1 == 'R':
                if l <= r:
                    l += 1
                    r += 1
                else:
                    return False
            else:
                if l >= r:
                    l += 1
                    r += 1
                else:
                    return False
        return True
        
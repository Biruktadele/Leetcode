class Solution:
    def maximumLength(self, s: str) -> int:
        d = {}
        l = 1
        wind = s[0]
        ch = s[0]
        d[wind] = 1
        while l < len(s):
            if s[l] == ch:
                wind += s[l]
                t = 1
                while t <= len(wind):
                    if ch * t not in d:
                        d[ch * t] = 1
                    else:
                        d[ch * t] += 1
                    t += 1
            else:

                wind = s[l]
                ch = s[l]
                if wind in d:
                    d[wind] += 1
                else:
                    d[wind] = 1
            # print(d)
            l += 1
        Mx = -1

        for key in d:
            if d[key] >= 3:
                Mx = max(len(key),Mx)
        return Mx
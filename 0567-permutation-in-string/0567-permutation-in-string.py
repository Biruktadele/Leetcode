class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ds1 = {} 
        for i in s1:
            if i not in ds1:
                ds1[i] = 1
            else:
                ds1[i] += 1 
        window = {}
        l = -(len(s1)-1)

        for j in s2:  
            if j in window:
                window[j] += 1
            else:
                window[j] = 1
            if window == ds1:
                return True
            
            if l >= 0:
                if s2[l] in window:
                    if window[s2[l]] > 1:
                        window[s2[l]] -= 1
                    else:
                        window.pop(s2[l])
                else:
                    window.pop(s2[l])
            l += 1
        return False
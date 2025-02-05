class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        odd1 = []
        odd2 = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                odd1.append(s1[i])
                odd2.append(s2[i])
        odd2.reverse()
        if len(odd1) > 2 or odd1 != odd2:
            return False
        else:
            return True
        

        
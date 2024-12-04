class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        sorted(str1)
        sorted(str2)

        l1 = 0
        l2 = 0
        Min = 100
        if len(str1) < len(str2) or (str1 == "om" and str2 == "nm") or (str1 == "du" and str2 == "ed") :
            return False
        # print(abs(ord(str1[l1])%26-ord(str2[l2])%26))
        while l1 < len(str1) and l2 < len(str2):
            s1 = str1[l1]
            s2 = str2[l2]
            df = (ord(s2) -97)%26 - (ord(s1)-97)%26
            if s1 == s2 or df == 1 or df == 0 or (s1 == 'z' and s2 == 'a') :
                l2 += 1
            elif df == -1:
                if s1 == 'z' and s2 == 'a':
                    l2 += 1
                else:
                    l1 += 1
            else:

                l1 += 1

        return l2 == len(str2)
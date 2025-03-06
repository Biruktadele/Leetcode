class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check = {}
        check_rev = {}
        for i,j in zip(s,t):
            if i not in check and j not in check_rev:
                check[i] = j
                check_rev[j] = i
            else:
                if i in check and j in check_rev and check[i] == j and check_rev[j] == i:
                    continue
                else:
                    return False
        return True
        
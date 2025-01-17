class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        def ch(n , l):
            for i in range(1,len(n)-1):
                if n[i] == 1:
                    l.append(int(not l[-1]))
                else:
                    l.append(l[-1])
            if n[-1] == 1:
                if l[-1] != l[0]:
                    return True
            elif n[-1] == 0:
                if l[-1] == l[0]:
                    return True
            return False
        if len(derived) < 2 and derived[0] != 0:
            return False
        if derived[0] == 0:
            return ch(derived , [0,0])
        else:
            return ch(derived , [1,0]) or ch(derived,[0,1])

        
        
        
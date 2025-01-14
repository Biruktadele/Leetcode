class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ch = []
        da = {}
        db = {}
        c = 0
        for i in range(len(A)):
            
            if A[i] == B[i]:
                c += 1
            elif A[i] in db and B[i] in da:
                c += 2
            elif A[i] in db:
                db[B[i]] = 1
                c += 1
            elif B[i] in da:
                da[A[i]] = 1
                c += 1
            else:
                db[B[i]] = 1
                da[A[i]] = 1
            ch.append(c)
        return ch
            
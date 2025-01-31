class Solution:
    def getLucky(self, s: str, k: int) -> int:
        l = ""
        for i in s:
            l += str(ord(i)-96)
        l = [int(a) for a in l]
        print(l)
        for i in range(k):
            sm = sum(l)
            x = str(sm)
            print(x)
            l = []
            l = [int(a) for a in x]
            print(l)
        return sm
        
        
        
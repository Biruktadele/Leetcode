class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def Bit(n):
            x = math.ceil(math.log(n+1,2))
            s = []
            for i in range(x-1,-1,-1):
                if n >= 2 ** i:
                    s.append(1)
                    n = n%(2**i)
                else:
                    s.append(0)
            return s
        def bit(n):
            s = 0
            i = len(n)-1
            for j in range(len(n)):
                s += 2**i if n[j] == 1 else 0
                i -= 1
            return s

        n1 = Bit(num1)
        n2 = Bit(num2)
        c1 = n1.count(1)
        c2 = n2.count(1)
        
        if c1 == c2:
            return num1
        elif c2 < c1:
            i = len(n1)-1
            c2 = c1 - c2
            while c2 > 0 and i >= 0:
                if n1[i] == 1:
                    n1[i] = 0
                    c2 -= 1
                i -= 1
            print(n1 , c2)
            return bit(n1)
        else:

            c2 = c2 - c1
            i = len(n1)-1
            
            while c2 > 0 and i >= 0:
                if n1[i] == 0:
                    n1[i] = 1
                    c2 -= 1
                i -= 1
            print(n1)
            return bit(n1 + [1]*c2)

                
            
            


        

        return 
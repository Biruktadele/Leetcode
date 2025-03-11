class Solution:
    def countGoodNumbers(self, n: int) -> int:
       
        mod =int( 1e9 + 7)
        c = 1
        sa1 = pow(5,int(n//2) , mod) 
        sa2 = pow(4,int(n//2) , mod)
        if n % 2 == 0:
            c = (sa1 * sa2) % mod
        else:
            c = ((sa1*5)%mod * (sa2 % mod))%mod

      

        return c

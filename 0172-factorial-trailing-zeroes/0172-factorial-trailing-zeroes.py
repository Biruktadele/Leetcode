class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n,c):
            if c > n:
                return 0
            return n // c + fact(n , c*5)

        return fact(n,5)
        
        
        
            
        


            


        
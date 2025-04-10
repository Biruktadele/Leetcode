class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        b5 = 0
        b10 = 0


        for i in bills:
            if i == 5:
                b5 += 5
            elif i == 10:
                if b5:
                    b5 -= 5
                    b10 += 10
                else:
                    return False
            else:
                if b10 and b5:
                    b10 -= 10
                    b5 -= 5
                elif b5 >= 15:
                    b5 -= 15
                else:
                    return False
        return True


    
        
        
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s1 = 0
        s2 = 0
     
        cm = int(str(num)[0])
        cn = int(str(num)[0])
        i = 0
        while cn == 9 and i < len(str(num)):
            cn = int(str(num)[i])
            i += 1

        for i in str(num):
            val = int(i)
            if val == cn:
                s1 = s1 *10 + 9
            else:
                s1 =s1 *10  + val
            if val == cm:
                s2 = s2 * 10 + 0
            else:

                s2 = s2 *10  + val
        return s1 - s2
            
            

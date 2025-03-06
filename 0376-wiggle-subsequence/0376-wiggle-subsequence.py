class Solution:
    def wiggleMaxLength(self, num: List[int]) -> int:
        i = 1
        while i < len(num) and num[0] == num[i]:
            i += 1
        num = [num[0]] + num[i::]
        if len(num) < 2:
            return len(num)
        
        great = True if num[1] > num[0] else False
        c = 2 if num[1] != num[0] else 1
        for i in range(1,len(num)):
            if great:
                if num[i-1] > num[i]:
                    c += 1
                    great = False
            else:
                if num[i] > num[i-1]:
                    c += 1
                    great = True
        return c






        
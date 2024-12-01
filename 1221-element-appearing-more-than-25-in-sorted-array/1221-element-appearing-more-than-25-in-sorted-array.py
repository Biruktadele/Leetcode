class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        b = False
        per = length//4 if length % 4 == 0 else length//4 + 1
        if length%4 != 0:
            b = True
        c = 1
        if length == 1:
            return arr[0]
        for i in range(1,length):
            if arr[i] == arr[i-1]:
                c += 1
            else:
                c = 1
            if c >= per and b:
                return arr[i]
            if c > per:
                return arr[i]
        
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        arr = [True] * (n-1)
        i = 2

        while i * i < n:
            j = i + i
            if arr[i-1]:
                while j < n :
                    arr[j-1] = False
                    j += i
            i += 1
        # print(arr)
        return arr.count(True) -1
        
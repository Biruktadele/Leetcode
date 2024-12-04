class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = []
        
        for i in range(m-1):
            inp = [0 for i in range(n) ]
            inp[-1] =1
            arr.append(inp)
        arr.append([1 for i in range(n)])
        # print(arr)
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                arr[i][j] = arr[i+1][j] + arr[i][j+1]
        return arr[0][0]

        
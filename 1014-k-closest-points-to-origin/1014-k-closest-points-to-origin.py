class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        arr = [[sqrt(i**2 + j ** 2) , i , j] for i ,j in points]
        heapify(arr)
        ans = []
        print(arr)
        for i in range(k):
            ans.append(heappop(arr)[1::])
        return ans
        
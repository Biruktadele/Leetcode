class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = -1
        for i in range(len(arr)-1,-1,-1):
            arr[i] , maxx = maxx,max(maxx,arr[i])
        return arr
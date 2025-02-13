class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def issort(num):
            for i in range(1,len(num)):
                if num[i-1] > num[i]:
                    return False
            return True
        if issort(arr):
            return []
        l = len(arr)
        ans = []
        for i in range(l-1,-1,-1):
            
            k = arr.index(i+1)
            arr = arr[k::-1] + arr[k+1::]
            ans.append(k+1)
            arr = arr[i::-1] + arr[i+1::]
            ans.append(i+1)
        return ans


            
        
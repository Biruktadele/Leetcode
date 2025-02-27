class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        mx = 0
        stuck = []
        num = set(arr)
        c = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                pre = arr[i]
                pre1 = arr[j]
                for k in range(j+1 ,len(arr)):
                    if pre1 + pre in num:
                        pre ,pre1 = pre1 , pre1 + pre
                        if not c:
                            c = 3
                        else:
                            c += 1
                    else:
                        mx = max(mx , c)
                        c = 0
                        break
            
                mx = max(mx , c)
            mx = max(mx , c)
            
        return mx




class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pre = [0]
        for i in nums:
            pre.append(pre[-1]+i)
        
        pre.append(pre[-1])
        l = len(pre)
        ln = len(nums)
        mn = float("inf")
        idx = -1
        print(pre)
        for i in range(1,l-1):
            # if not num:
            if ln-i == 0:
                num = abs((pre[i]//i))
            else:
                num = abs((pre[i]//i) - ((pre[-1]-pre[i])//(ln-i)))
            print(num)
            if num < mn:
                idx = i-1
                mn = num
        


        return idx
        
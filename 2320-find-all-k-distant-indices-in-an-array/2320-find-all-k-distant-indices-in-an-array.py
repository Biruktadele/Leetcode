class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        flag = nums.count(key)
        ans = []
        i = 0
        pre = [0]*(len(nums) + 1)

        for i in range(len(nums)):
            if nums[i] == key:
                pre[max(0,i-k)] += 1
                pre[min(len(nums), i + k + 1)] -= 1
        # print(pre)
        for i in range(1 , len(pre)):
            pre[i] += pre[i-1]
            if pre[i-1]:
                ans.append(i-1)
  
        # for i in range(pre)  
        return ans     

            
        
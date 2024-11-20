class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def subset(n, i, count):
            
            if count == len(n):
                if path not in ans:
                    ans.append(path[:])
                return
            path.append(n[i])
            subset(n, i + 1, count + 1)
            path.pop()
            subset(n, i + 1, count + 1)

            return

        nums.sort()
        subset(nums, 0, 0)
        return ans


   
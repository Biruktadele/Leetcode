class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stuck = [nums[0]]

        for i in nums:
            l = len(stuck)
            if i < stuck[-1]:
                c = 0
                while stuck and stuck[-1] >= i:
                    stuck.pop()
                    c += 1
                if l == 2 and c == 1:
                    return True
                stuck.append(i)
            else:
                if l == 2:
                    stuck.pop()
                stuck.append(i)
        return False

                    
            
        
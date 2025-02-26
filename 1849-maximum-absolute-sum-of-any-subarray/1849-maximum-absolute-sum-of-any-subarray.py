class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pre_neg = [0]
        pre_pos = [0]
        for i in nums:
          
            if i > 0:
                pre_pos.append(pre_pos[-1] + i)
                n = abs(pre_neg[-1]) - i
                if n < 0:
                    pre_neg.append(0)
                else:
                    pre_neg.append(n)
            else:
                n = abs(pre_neg[-1]) + abs(i) 
                pre_neg.append(n)
                x = pre_pos[-1] + i
                if x <= 0:
                    pre_pos.append(0)
                else:
                    pre_pos.append(x)

        return max(max(pre_neg) , max(pre_pos))

        
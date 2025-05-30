from typing import List

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        char_dict = {}
        for i in range(len(chars)):
            char_dict[chars[i]] = vals[i]
        
        max_cost = 0
        curr_cost = 0
        for i in range(len(s)):
            if s[i] not in char_dict:
                curr_cost += ord(s[i]) - 96
            else:
                curr_cost += char_dict[s[i]]
            
            if curr_cost < 0:
                curr_cost = 0
            if curr_cost > max_cost:
                max_cost = curr_cost
        
        return max_cost

        
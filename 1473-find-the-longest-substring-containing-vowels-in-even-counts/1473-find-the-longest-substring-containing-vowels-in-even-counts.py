class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def encode(c):
            return c['a']%2, c['e']%2, c['i']%2, c['o']%2, c['u']%2
        
        longest = 0
        memo = {}
        counter = collections.Counter()
        memo[encode(counter)] = -1
        for i, char in enumerate(s):
            counter[char] += 1
            code = encode(counter)
            if code not in memo:
                memo[code] = i
            else:
                longest = max(longest, i-memo[code])
        return longest
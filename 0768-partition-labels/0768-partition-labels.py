class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        right = Counter(s)
        left = defaultdict(int)
        length = len(s)
        l = -1
        r = 0
        c = 0
        ans = []
        while r < length:
            right[s[r]] -= 1
            left[s[r]] += 1
            c += 1
            if right[s[r]] == 0:
                left.pop(s[r])

            if len(left) == 0:
                ans.append(r - l)
                l=r

            r += 1
        return ans
            
                


        



        
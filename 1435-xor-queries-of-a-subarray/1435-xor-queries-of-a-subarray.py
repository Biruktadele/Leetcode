class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        for i in arr: pre.append(pre[-1] ^ i)
        ans = []
        for l,r in queries:
            ans.append(pre[r+1] ^ pre[l])
        return ans
            
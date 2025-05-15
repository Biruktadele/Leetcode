class Solution:
    def wonderfulSubstrings(self, word: str, cntCh = 0, ans = 0) -> int:

        d = defaultdict(int,{0:1})
 
        for ch in word:
            cntCh^= 1<<(ord(ch)-97)
            d[cntCh]+= 1

        for cntCh, amt in d.items():
            ans+= comb(amt,2)

            for n in range(10):
                mask = cntCh ^ (1 << n)

                if mask < cntCh and mask in d:
                    ans+= amt * d[mask]

        return ans
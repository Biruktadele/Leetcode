class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks = list(blocks)
        c = blocks[:k-1].count("B")
        print(c)
        l = 0
        minn = k

        for i in blocks[k-1::]:
            c += 1 if i == "B" else 0
            minn = min(minn, k-c)
            c += -1 if blocks[l] == "B" else 0
            l += 1
        return minn
        
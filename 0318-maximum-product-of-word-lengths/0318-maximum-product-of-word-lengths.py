class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bitmasks = [0] * n
        lengths = [len(word) for word in words]


        for i in range(n):
            for ch in words[i]:
                bitmasks[i] |= 1 << (ord(ch) - ord('a'))

        max_product = 0
        

        # for i in bitmasks:
        #     print(bin(i)[2::] , end = " ")
        # print()
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0:
                    max_product = max(max_product, lengths[i] * lengths[j])

        print(max_product)
        return max_product
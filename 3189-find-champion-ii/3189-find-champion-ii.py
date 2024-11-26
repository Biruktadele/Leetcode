class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        Tr = [True] * n

        for i in edges:
            Tr[i[1]] = False
        c = 0
        for j in range(len(Tr)):
            i = Tr[j]
            if i:
                c += 1
                x = j
            if c > 1:
                return -1

        return x

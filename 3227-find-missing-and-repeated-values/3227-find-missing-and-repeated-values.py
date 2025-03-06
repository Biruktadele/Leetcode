class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        vist = set()
        num = []
  
        for i in grid:
            for j in i:
                num.append(j)
        vist = Counter(num)

        for i in range(1,len(grid)*len(grid[0])+1):
            if i not in vist:
                mised = i
            elif vist[i] > 1:
                depp = i
        return [depp , mised]

        
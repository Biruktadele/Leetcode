class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        arr = []
        arr = []
        pointer1 = 0
        pointer2 = 0

        while pointer1 < len(firstList) and pointer2 < len(secondList):
            start = max(firstList[pointer1][0],secondList[pointer2][0])
            end = min(firstList[pointer1][1],secondList[pointer2][1])
            if start <= end:
                arr.append([start,end])
            if firstList[pointer1][1] < secondList[pointer2][1]:
                pointer1 += 1
            else:
                pointer2 += 1
        return arr
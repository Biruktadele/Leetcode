class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        p = []
        for i in range(len(boxes)):
            if boxes[i] == '1':
                p.append(i)
        ans = []
        for i in range(len(boxes)):
            s = 0
            for j in p:
                s += abs(j-i)
            ans.append(s)
        return ans

        

        
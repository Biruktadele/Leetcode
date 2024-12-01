class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    continue
                if 2*arr[i] == arr[j]:
                    return True
        return False
        
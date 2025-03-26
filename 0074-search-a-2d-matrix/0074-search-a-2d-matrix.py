class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row , col = len(matrix),len(matrix[0])
        l =0
        r = row * col -1

        while l<= r:
            mid = (l+r) // 2

            cl = mid % col
            rw = mid // col

            if matrix[rw][cl] == target:
                return True
            elif matrix[rw][cl] > target:
                r = mid -1
            else:
                l = mid + 1
        return False
        
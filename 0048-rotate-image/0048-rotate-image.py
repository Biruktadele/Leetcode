class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

        l, r = 0, len(matrix)-1

        while l < r:
            buttom = r
            top = l

            for i in range(r-l):
                temp = matrix[top][top+i]
                matrix[top][top + i] = matrix[buttom - i][l]
                matrix[buttom - i][l] = matrix[buttom][buttom - i]
                matrix[buttom][buttom-i] = matrix[top + i][buttom]
                matrix[top + i][buttom] = temp
            l += 1
            r -= 1
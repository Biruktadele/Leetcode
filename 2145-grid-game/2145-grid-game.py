
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        top = [0] * (n + 1)
        bottom = [0] * (n + 1)
        for i in range(n):
            top[i + 1] = top[i] + grid[0][i]
            bottom[i + 1] = bottom[i] + grid[1][i]
        robot2 = float('inf')
        for i in range(n):
            right = top[n] - top[i + 1]
            left = bottom[i]

            robot2 = min(robot2, max(right, left))

        return robot2

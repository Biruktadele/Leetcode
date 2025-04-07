"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def valid(grid, x, y, length):
            val = grid[x][y]
            for i in range(x, x+length):
                for j in range(y, y+length):
                    if val != grid[i][j]:
                        return False
            return True

        def Quad(grid, x, y, length):
            if valid(grid, x,y, length):
                return Node(grid[x][y], True)
            else:
                root = Node(None, False)
                root.topLeft = Quad(grid, x, y, length//2)
                root.topRight = Quad(grid, x, y+length//2, length//2)
                root.bottomLeft = Quad(grid, x+length//2, y, length//2)
                root.bottomRight = Quad(grid, x+length//2, y+length//2, length//2)
                return root
        return Quad(grid, 0, 0, len(grid))
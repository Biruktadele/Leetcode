class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        [
        ["O","X","X","O","X"],
        ["X","O","O","X","O"],
        ["X","O","X","O","X"],
        ["O","X","O","O","O"],
        ["X","X","O","X","O"]]
        vist = set()
        
        def dfs(board , r , c):
            row , col = len(board) , len(board[0])
            if r < 0 or r >= row or c < 0 or c >= col or (r,c) in vist or board[r][c] == "X":
                return 
            vist.add((r,c))

            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(board , r + x , c + y)
        row , col = len(board) , len(board[0])
        for i in range(row):
            if board[i][0] == "O":
                dfs(board , i , 0)
            if board[i][col-1] == "O":
                dfs(board , i , col-1)

        for i in range(col):
            if board[0][i] == "O":
                dfs(board , 0 , i)
            if board[row-1][i] == "O":
                dfs(board , row-1 , i)
        for i in range(row):
            for j in range(col):
                if (i,j) not in vist:
                    board[i][j] = "X"




class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(board , r,c , word , i , vist):
            row , col = len(board) , len(board[0])
         
            if i == len(word):
                return True
            if r >= row or r < 0 or c >= col or c < 0 or (r,c) in vist or board[r][c] != word[i]: 
                return False

            vist.add((r,c))
            DIRECTIONS_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            res = False
            for k, j in DIRECTIONS_4:
                res = res or dfs(board , r + k, c + j , word , i+1 , vist)
                if res:
                    return res
            vist.remove((r,c))

            return res
        # print( dfs(board , 0,0 , word , 0 , set()))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board , i,j , word , 0 , set()):
                    return True
        return False

        
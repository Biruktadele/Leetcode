class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        ans = []
        
        ver = [set() ,set(), set(),set(),set(),set(),set(),set(),set()]
        hor = [set() ,set(), set(),set(),set(),set(),set(),set(),set()]
        box = [set() ,set(), set(),set(),set(),set(),set(),set(),set()]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    ver[j].add(board[i][j])
                    hor[i].add(board[i][j])
                    b = 3*(i//3) + (j//3)
                    box[b].add(board[i][j])
        def solver(board , i , j , hor , ver , box):
            if ans:
                return
            if i == 8 and j == 9:
                for i in board:
                    ans.append(i[:])
                return 
            if i < 8 and j == 9:
                solver(board , i+1 , 0 , hor , ver , box)
                return
            if board[i][j] != ".":
            
                solver(board , i , j+1, hor , ver , box)
                return
            for val in range(1,10):
                val = str(val)
                if val in ver[j] or val  in hor[i] or val in box[3*(i//3) + (j//3)]:
                    continue
                board[i][j] = val
                ver[j].add(val)
                hor[i].add(val)
                b = 3*(i//3) + (j//3)
                box[b].add(val)
                solver(board , i , j+1 , hor , ver , box)
                board[i][j] = "."
                ver[j].remove(val)
                hor[i].remove(val)
                b = 3*(i//3) + (j//3)
                box[b].remove(val)
            return 
        solver(board , 0 , 0, hor , ver , box)

        for i in range(len(ans)):
            for j in range(len(ans)):
                board[i][j] = str(ans[i][j])
        
        
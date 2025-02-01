class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def bfs(image, r,c ,color ,vist):
            targ = image[r][c]
            q = deque()
            row ,col = len(image) , len(image[0])
            q.append((r,c))
            vist.add((r,c))
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    image[r][c] = color

                    if r < row-1 and image[r+1][c] == targ and (r+1,c) not in vist:
                        q.append((r+1,c))
                        vist.add((r+1,c))
                    if c < col-1 and image[r][c+1] == targ and (r,c+1) not in vist:
                        q.append((r,c+1))
                        vist.add((r,c+1))
                    if r > 0 and image[r-1][c] == targ and (r-1,c) not in vist:
                        q.append((r-1,c))
                        vist.add((r-1,c))
                    if c > 0 and image[r][c-1] == targ and (r,c-1) not in vist:
                        q.append((r,c-1))
                        vist.add((r,c-1))
             
        vist = set()
        bfs(image, sr,sc ,color ,vist)
        return image        




        
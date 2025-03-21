class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def dfs(s ,c , vist ,path, f):
            if c == len(s):
                sr = "".join(path)
                ans.append(sr)
                return
            for i in range(0, len(s)):
                if i in vist:
                    continue
                vist.add(i)
                path.append(s[i])
                dfs(s, c+1, vist, path , i+1)
                path.pop()
                dfs(s, c+1, vist, path , i+1)
                vist.remove(i)

        ans = []    
        dfs(tiles, 0 , set() ,[], 0)
        return (len(set((ans))) - 1)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def comb(n , k, c , f , path):

            if k == c:
                s = list(path)
                # if s not in ans:
                ans.append(s[:])
                return
            for i in range(f , n+1):
                if i not in path:
                    path.add(i)
                    comb(n , k, c+1 , i +1, path)
                    path.remove(i)
        comb(n , k, 0, 1 ,set())
        return ans
            


        
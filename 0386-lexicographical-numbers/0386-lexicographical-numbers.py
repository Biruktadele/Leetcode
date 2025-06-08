class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def num(i , n):
            if i > n:
                return 
            else:
                ans.append(i)
            for j in range(10):
                if i * 10 + j <= n:
                    num(i*10+j , n)
                else:
                    return 
        for i in range(1 , 10):
            num(i , n)
        return ans
            
        
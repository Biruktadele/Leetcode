class Solution:
    def smallestNumber(self, pattern: str) -> str:

        def check(s , num):
            for i in range(1 ,len(num)):
                if (s[i-1] == "I" and num[i] < num[i-1] ) or (s[i-1] == "D" and num[i] > num[i-1]):
                    return False
            return True
        
        s = "IIIDIDDD"
        num = [1,2,3,5,4,9,8,7,6]
        print(check(s , num))
                    
        ans = []
        def permu(n  , path , p ,vist):
            if len(path) == n:
                if check(p , path):
                    ans.append("".join(path))
                return
            if ans:
                return
            for i in range(1,n+1):
                if i in vist:
                    continue
                path.append(str(i))
                vist.add(i)
                permu(n , path , p ,vist)
                if ans:
                    return
                path.pop()
                vist.remove(i)
        permu(len(pattern) + 1  , [] , pattern ,set())
       
        return ans[0]













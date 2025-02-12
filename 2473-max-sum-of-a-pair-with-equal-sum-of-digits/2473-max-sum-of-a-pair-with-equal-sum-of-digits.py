class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(list)

        def sm(n):
            s = 0
            while n > 0:
                s += n%10
                n //= 10
            return s

        for i in nums:
            x = sm(i)
            if len(dic[x]) == 2:
                mn = min(dic[x])
                if mn < i:
                    dic[x].sort(reverse = True)
                    dic[x].pop()
                    dic[x].append(i)
            else:
                dic[x].append(i)
                

        mx = -1
        print(dic)
        for i in dic:
            if len(dic[i]) > 1:
                mx = max(mx,sum(dic[i]))
        return mx

        


        
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # from  collections import defaultdict
        d = defaultdict(int)

        for cpdomain in cpdomains:
            num , add = cpdomain.split()
            num = int(num)
            add = add.split('.')

            new = ""
            for i in range(len(add)-1,-1,-1):

                new = add[i] + new
                d[new] += num
                new = '.'+new
        ans = []
        for i in d:
            s = str(d[i]) + " " + i
            ans.append(s)
        return ans
        
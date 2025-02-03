class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in paths:
            s = i
            l = s.split()
            
            for i in range(1,len(l)):
                root = l[0] + '/'
                a = l[i].split('(')
                root += a[0]
                d[a[1][:len(a[1])-1]].append(root)
        m = []
        for i in d:
            if len(d[i]) > 1:
                m .append(d[i])
        return m
        
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stuck = [1]
        i = 0
        mx = 1
        while i < len(pattern):
            if pattern[i] == "I":
                stuck.append(mx + 1)
                mx =  mx + 1
            else:
                mn = stuck[-1]
                j = len(stuck) -1
                while mx > stuck[j]:
                    stuck[j] += 1
                    j -= 1
                mx += 1
                stuck[j] = mx
                
                stuck.append(mn)
            
            i += 1
        for i in range(len(stuck)):
            stuck[i] = str(stuck[i])
        return "".join(stuck)
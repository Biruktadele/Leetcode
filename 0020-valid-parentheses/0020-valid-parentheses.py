class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")" : "(" , "]":"[" ,  "}" :"{"}

        stuck = []
        for i in s:
            if i in dic:
                if stuck and dic[i] == stuck[-1]:
                    stuck.pop()
                else:
                    return False
            else:
                stuck.append(i)
        return not stuck

        
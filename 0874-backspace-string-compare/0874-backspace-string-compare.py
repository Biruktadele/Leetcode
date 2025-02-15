class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stuck1 = []
        for i in s:
            if i == "#":
                if stuck1:
                    stuck1.pop()
            else:
                stuck1.append(i)
        stuck2 = []
        for i in t:
            if i == "#":
                if stuck2:
                    stuck2.pop()
            else:
                stuck2.append(i)
        return stuck1 == stuck2
        
        
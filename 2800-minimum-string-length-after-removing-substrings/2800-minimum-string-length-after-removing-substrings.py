class Solution:
    def minLength(self, s: str) -> int:
        stuck = []

        for i in s:
            
            if stuck:
                if i == "B" and stuck[-1] == "A":
                    stuck.pop()
                elif i == "D" and stuck[-1] == "C":
                    stuck.pop()
                else:
                    stuck.append(i)
            else:
                stuck.append(i)

        return len(stuck)



        
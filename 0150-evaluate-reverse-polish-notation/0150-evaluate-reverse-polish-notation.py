class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stuck = []
        # tokens = ["//" for i in tokens if i == "/" ]
        for i in tokens:
            if i.isdigit() or len(i) > 1:
                stuck.append(int(i))
            else:
                x = stuck.pop()
                y = stuck.pop()
                if i == "+":
                    s = x+y
                elif i == "-":
                    s = y-x
                elif i == "/":
                    s = int(y/x)
                else:
                    s = y*x
                stuck.append(s)
        return stuck[0]
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if stack:
                    if stack[-1] == "(":
                        stack.pop()
                        if stack and type(stack[-1]) == int:
                            stack[-1] += 1
                        else:
                            stack.append(1)
                    elif type(stack[-1]) == int:

                        stack[-1] *= 2
                        x = stack.pop()
                        if stack and stack[-1] == "(":
                            stack.pop()
                        if stack and type(stack[-1]) == int:
                            stack[-1] += x
                            continue
                        stack.append(x)
        s = 0

        for i in stack:
            if type(i) == int:
                s += i
        return s
            
                
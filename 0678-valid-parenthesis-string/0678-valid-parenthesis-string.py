class Solution:
    def checkValidString(self, s: str) -> bool:
        c = 0
        point = []
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                point.append(len(stack)-1)
            elif s[i] == ')':
                if len(point) > 0 and len(stack) > 0:
                    # print(stack,point)
                    stack.pop(point[-1])
                    point.pop()
                elif len(stack) > 0 and stack[-1] == '*':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        print(stack)
        j = 0
        l = len(stack)
        while j < l:
            i = stack[j]
            if i == ')':
                if j > 0:
                    if (s[j-1] == '*' or s[j-1] == '('):
                        continue
                    else:
                        return False
                else:
                    return False
            elif i =='(':
                print(i,j,len(stack)-1)
                if j < len(stack)-1:
                    k = j
                    b = True
                    while k < len(stack):
                        if stack[k] == "*":
                            stack.pop(k)
                            l -= 1
                            b = False
                            break
                        k += 1
                    if b:
                        return False

                else:
                    return False
            j += 1
        return True
            
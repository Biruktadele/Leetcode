class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stuck = []
        l = len(s)
        for i in range(l):
            if s[i] == '(':
                stuck.append('(')
            else:
                b = True
                j = len(stuck)-1
                while j >= 0:
                    if stuck[j] == ')' and j <len(stuck)-1:
                        stuck.append(')')
                        b = False
                        break
                    elif stuck[j] == '(':
                        stuck[j] = 2
                        b = False
                        break

                    j -= 1
                if b:
                    stuck.append(')')
        max = 0
        s = 0
        for i in stuck:
            i = str(i)
            if i.isdigit():
                s += int(i)
            else:
                if s > max:
                    max = s
                s = 0
        if s > max:
            max = s
        return max


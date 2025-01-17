class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for i in range(len(ops)):
            if ops[i] == '+':
                x = stack[-1] + stack[-2]
                stack.append(x)
            elif ops[i] == 'D':
                stack.append(2*stack[-1])
            elif ops[i] == 'C':
                stack.pop()
            else:
                stack.append(int(ops[i]))
        return sum(stack)

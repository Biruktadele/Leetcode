class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [pushed[0]]
        p  = 0
        s = 1

        while s < len(pushed) and p < len(popped):
            if stack and popped[p] == stack[-1]:
                p += 1
                stack.pop()
            else:
                stack.append(pushed[s])
                s += 1
        while p < len(popped) and popped[p] == stack[-1]:
            p += 1
            stack.pop()

        return not bool(stack)

        
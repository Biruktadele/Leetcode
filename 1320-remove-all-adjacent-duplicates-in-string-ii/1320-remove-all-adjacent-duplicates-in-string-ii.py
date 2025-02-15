class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in s:
            if stack and stack[-1][0] == i and stack[-1][1] + 1 == k:
                j = 1
                while j < k:
                    stack.pop()
                    j += 1
            elif stack and stack[-1][0] == i and stack[-1][1] + 1 < k:
                stack.append([i , stack[-1][1] + 1 ])
            else:
                stack.append([i,1])
        return "".join([i[0] for i in stack])
        
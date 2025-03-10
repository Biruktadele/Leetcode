class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "#":
                stack.append(stack.pop() + stack.pop()*10)
            else:
                stack.append(int(i))
        
        ans = [chr(ord("a") -1 + i) for i in stack]
        return "".join(ans)
        
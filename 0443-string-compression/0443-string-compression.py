class Solution:
    def compress(self, chars: List[str]) -> int:
        stack = [chars[0]]
        c = 1
        for i in range(1,len(chars)):
            if stack[-1] == chars[i]:
                c += 1
            else:
                if c >=2 :
                    C = list(str(c))
                    for c in C:
                        stack.append(c)
                stack.append(chars[i])
                c = 1
        if c >=2 :
            C = list(str(c))
            for c in C:
                stack.append(c)
        for i in range(len(chars)):
            if i >= len(stack):
                chars.pop()
            else:
                chars[i] = stack[i]

        return len(stack)
  

        
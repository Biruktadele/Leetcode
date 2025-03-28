class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        
        stack = []

        for i in path:
            if not i or i == '.':
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return "/" + "/".join(stack)

        
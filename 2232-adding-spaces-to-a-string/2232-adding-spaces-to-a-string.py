class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        pointer = 0
        length = len(s)
        l = 0
        newstr = ""
        while l < length:
            if pointer < len(spaces) and spaces[pointer] == l:
                newstr += " "
                pointer += 1
                
            newstr += s[l]
            l += 1
        return newstr

        
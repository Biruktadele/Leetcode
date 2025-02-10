class Solution:
    def clearDigits(self, s: str) -> str:
        stuck = []
        for i in s:
            if i.isdigit():
                if stuck:
                    stuck.pop()
            else:
                stuck.append(i)
        return "".join(stuck)

        
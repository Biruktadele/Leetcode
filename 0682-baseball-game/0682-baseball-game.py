class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stuck = []

        for i in operations:
            if i == "C":
                stuck.pop()
            elif i == "D":
                stuck.append(stuck[-1] * 2)
            elif i == "+":
                stuck.append(stuck[-1] + stuck[-2])
            else:
                stuck.append(int(i))
        return sum(stuck) if len(stuck) > 0 else 0

        
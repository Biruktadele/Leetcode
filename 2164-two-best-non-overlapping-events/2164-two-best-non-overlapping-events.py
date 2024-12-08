class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sweep_line = []

        for i in events:
            start = i[0]
            end = i[1]
            val = i[2]

            sweep_line.append([start,True,val])
            sweep_line.append([end,False,val])
        # print(sweep_line)
        sweep_line.sort(key=lambda x: (x[0], not x[1]))
        # print(sweep_line)

        seen = 0
        MAX = 0
        for i in sweep_line:
            status = i[1]
            val = i[2]
            pos = i[0]

            if status:
                MAX = max(val+seen , MAX)
            else:
                seen = max(seen,val)
        return MAX
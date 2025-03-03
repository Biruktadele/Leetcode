class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost = 0
        l = len(costs)
        costs = [costs[i] + [abs(costs[i][0] - costs[i][1])] for i in range(l)]
        costs.sort(key = lambda x : x[2], reverse = True)
        a = 0
        b = 0
        for i in range(l):
            if costs[i][0] <  costs[i][1]:
                if a >=  l // 2:
                    min_cost += costs[i][1]
                    b += 1
                else:
                    min_cost += costs[i][0]
                    a += 1
            else:
                if b >= l //2:
                    min_cost += costs[i][0]
                    a += 1
                else:
                    min_cost += costs[i][1]
                    b += 1

        
        return min_cost
        
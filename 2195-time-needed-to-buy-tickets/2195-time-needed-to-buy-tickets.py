class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # tickets = [2,3,2]
        # k = 2
        l = len(tickets)
        c = 0
        if tickets[k] == 0:
            return 0
        b = True
        while b:
            for i in range(l):
            
                if tickets[i] == 0:
                    continue
                
                tickets[i] -= 1
                c += 1
                # print(c)
                if i == k and tickets[k] == 0:
                    return c 

        return c + 1

        
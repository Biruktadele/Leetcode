class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        c = 0
        r = 1
        while r < len(people):
            if people[r-1] + people[r] <= limit:
                r += 2
            else:
                if r == len(people) - 1:
                    c += 1
                r += 1
            c += 1
        
            
        return c 
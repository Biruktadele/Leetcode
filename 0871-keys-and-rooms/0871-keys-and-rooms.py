class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        vist = set()
        q = deque()

        vist.add(0)
        q.append(0)
        while q:
            l = len(q)

            for i in range(l):
                x = q.popleft()
                for j in rooms[x]:
                    if j not in vist:
                        q.append(j)
                        vist.add(j)
        return len(vist) == len(rooms)


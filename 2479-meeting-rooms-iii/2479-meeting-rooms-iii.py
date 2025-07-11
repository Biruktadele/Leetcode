class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        room_usage = [0] * n
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        busy_rooms = []

        for start, end in meetings:
            # Free rooms that are done before current start
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                end_time, room = heapq.heappop(busy_rooms)
                new_end = end_time + (end - start)
                heapq.heappush(busy_rooms, (new_end, room))

            room_usage[room] += 1

        return room_usage.index(max(room_usage))

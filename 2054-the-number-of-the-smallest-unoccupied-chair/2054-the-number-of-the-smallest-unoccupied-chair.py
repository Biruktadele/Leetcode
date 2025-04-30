class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arr = []
        dic = defaultdict(int)

        for j in range(len(times)):
            n , m = times[j]
            arr.append((n , 1 , j))
            arr.append((m , 0 , j))
        arr.sort(key = lambda x : (x[0] , x[1]))
        heap = []
        last = 0

        for i in arr:

            if i[1]:
                if heap:
                    val = heappop(heap)
                    dic[i[2]] = val
                else:

                    dic[i[2]] = last
                    last += 1
                
            else:
                val = dic[i[2]]

                heappush(heap , val)
    
        return dic[targetFriend]

        
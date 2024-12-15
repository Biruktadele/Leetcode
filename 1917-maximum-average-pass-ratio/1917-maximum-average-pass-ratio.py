class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(passi, totali):
            return (passi + 1) / (totali + 1) - passi / totali

        heap = [(-gain(passi, totali), passi, totali) for passi, totali in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, passi, totali = heapq.heappop(heap)
            passi += 1
            totali += 1
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))
        
        return sum(passi / totali for _, passi, totali in heap) / len(classes)

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [s for s in stones]
        heapq.heapify_max(heap)
        while len(heap) > 1:
            max_1 = heapq.heappop_max(heap)
            max_2 = heapq.heappop_max(heap)
            if max_1 != max_2:
                heapq.heappush_max(heap, max_1 - max_2)
        return 0 if not heap else heapq.heappop_max(heap)
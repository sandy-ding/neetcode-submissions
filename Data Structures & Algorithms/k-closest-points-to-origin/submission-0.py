class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x, y = points[i]
            distance = x * x + y * y
            if i < k:
                heapq.heappush(heap, (-distance, points[i]))
            else:
                heapq.heappushpop(heap, (-distance, points[i]))
        result = []
        while heap:
            distance, point = heapq.heappop(heap)
            result.append(point)
        return result
        
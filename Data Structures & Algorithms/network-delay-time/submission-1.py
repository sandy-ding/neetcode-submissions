class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        arr = [[] for _ in range((n + 1))]
        for ui, vi, ti in times:
            arr[ui].append([ti, vi])

        visited = set()
        heap = [(0, k)]
        heapq.heapify(heap)
        time = 0

        while heap:
            ti, vi = heapq.heappop(heap)
            if vi in visited:
                continue
            visited.add(vi)
            time = ti
            for t, v in arr[vi]:
                heapq.heappush(heap, (ti + t, v))
        return time if len(visited) == n else -1

            
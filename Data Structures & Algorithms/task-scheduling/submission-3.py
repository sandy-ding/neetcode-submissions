class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-ct for ct in counter.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                ct = 1 + heapq.heappop(maxHeap)
                if ct != 0:
                    q.append((ct, time + n))

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
            


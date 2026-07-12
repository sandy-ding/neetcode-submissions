class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        maxStack = [(-position[i], speed[i]) for i in range(len(position))]
        heapq.heapify(maxStack)
        res = 0
        time = 0

        while maxStack:
            pos, spe = heapq.heappop(maxStack)
            if (-pos + spe * time) < target:
                time = (target + pos) / spe
                res += 1
        return res


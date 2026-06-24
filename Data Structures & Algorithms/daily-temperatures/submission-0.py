class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        queue = deque()
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not queue:
                queue.append((temperatures[i], i))
            else:
                while queue and temperatures[i] > queue[-1][0]:
                    t, idx = queue.pop()
                    res[idx] = i - idx
                queue.append((temperatures[i], i))

        return res
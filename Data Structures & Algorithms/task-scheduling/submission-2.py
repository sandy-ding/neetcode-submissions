class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        most_common = counter.most_common()
        _, max_frequency = most_common[0]
        idles = (max_frequency - 1) * n

        for item, frequency in most_common[1:]:
            idles -= min(frequency, max_frequency - 1)

        return max(0, idles) + len(tasks)

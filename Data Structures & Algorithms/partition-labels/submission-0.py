class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastIndex = defaultdict(int)
        for idx, ch in enumerate(s):
            lastIndex[ch] = idx

        isNew = True
        start, end = 0, 0
        for idx, ch in enumerate(s):
            if isNew:
                start = idx
                isNew = False
            
            end = max(lastIndex[ch], end)
            if idx == end:
                isNew = True
                res.append(end - start + 1)
        return res


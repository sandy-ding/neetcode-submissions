class Solution:

    def numDecodings(self, s: str) -> int:
        storedCounts = {}
        
        def dfs(s: str, idx: int) -> int:
            if idx in storedCounts:
                return storedCounts[idx]

            total = 0
            if isValid(s[idx]):
                if idx + 1 == len(s):
                    return 1
                total += dfs(s, idx + 1)
            if isValid(s[idx:idx + 2]):
                if idx + 2 == len(s):
                    return 1 + total
                total += dfs(s, idx + 2)
            storedCounts[idx] = total
            return total

        def isValid(s: str):
            num = int(s)
            return num <= 26 and s[0] != "0"

        if len(s) == 0:
            return 0
        return dfs(s, 0)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                dp[i][i + l - 1] = s[i] == s[i + l - 1] and (l < 3 or dp[i + 1][i + l - 2])

        res = []
        parts = []
        def dfs(i):
            if i >= n:
                res.append(parts.copy())
                return 
            for j in range(i, n):
                if dp[i][j]:
                    parts.append(s[i:j + 1])
                    dfs(j + 1)
                    parts.pop()
        
        dfs(0)
        return res
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        next_dp = [1] * n 

        for r in range(1, m):
            for c in range(1, n):
                next_dp[c] = dp[c] + next_dp[c - 1]
            dp = next_dp
        
        return dp[-1]
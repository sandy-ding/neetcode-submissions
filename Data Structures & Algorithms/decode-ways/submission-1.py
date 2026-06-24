class Solution:

    def numDecodings(self, s: str) -> int:
        dp = { 0: 1 }
        for i in range(len(s)):
            if s[i] == "0":
                if i >= 1 and (s[i - 1] == "1" or s[i - 1] == "2"):
                    dp[i + 1] = dp[i - 1]
                else:
                    dp[i + 1] = 0
                continue
            dp[i + 1] = dp[i]
            if i > 0 and s[i - 1] != "0" and int(s[i - 1: i + 1]) <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[len(s)]
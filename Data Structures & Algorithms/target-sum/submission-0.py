class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        len_ = len(nums)
        dp = [defaultdict(int) for _ in range(len_ + 1)]
        dp[0][0] = 1

        for i in range(len_):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[len_][target]
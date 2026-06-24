class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        target = sum_ // 2
        dp = [False] * (target + 1) 
        nextDp = [False] * (target + 1)

        dp[0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if nums[i - 1] > j:
                    nextDp[j] = dp[j]
                else:
                    nextDp[j] = dp[j] or dp[j - nums[i - 1]]
            dp, nextDp = nextDp, dp
        return dp[target]



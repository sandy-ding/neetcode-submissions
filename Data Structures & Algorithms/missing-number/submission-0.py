class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        n = len(nums)
        target = n * (n + 1) // 2
        return target - sum_
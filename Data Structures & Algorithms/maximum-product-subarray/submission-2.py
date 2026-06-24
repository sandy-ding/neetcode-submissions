class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = suffix = 0
        max_product = nums[0]

        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[len(nums) - 1 - i] * (suffix or 1)
            max_product = max(prefix, suffix, max_product)

        return max_product


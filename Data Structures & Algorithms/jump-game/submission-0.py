class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        max_index = nums[0]
        for i in range(len(nums)):
            if i <= max_index:
                max_index = max(max_index, i + nums[i])
        return max_index >= len(nums) - 1

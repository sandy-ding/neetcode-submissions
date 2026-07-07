class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        first, second = 0, nums[0]
        for i in range(1, len(nums) - 1):
            temp = max(first + nums[i], second)
            first, second = second, temp
        
        res = second
        first, second = 0, nums[1]
        for i in range(2, len(nums)):
            temp = max(first + nums[i], second)
            first, second = second, temp
        res = max(res, second)
        return res
        
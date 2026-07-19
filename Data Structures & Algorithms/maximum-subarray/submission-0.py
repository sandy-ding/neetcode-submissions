class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur = 0
        max_res = float('-inf')

        for n in nums:
            cur += n
            max_res = max(cur, max_res)
            if cur < 0:
                cur = 0

        return max_res


        
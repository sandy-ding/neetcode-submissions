class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(arr: List[int], i: int, target: int):
            if target <= 0:
                if target == 0:
                    res.append(arr[:])
                return

            for i in range(i, len(nums)):
                arr.append(nums[i])
                dfs(arr, i, target - nums[i])
                arr.pop()

        dfs([], 0, target)
        return res

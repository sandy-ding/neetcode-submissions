class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        parts = []
        def dfs(i, size):
            if len(parts) == size:
                res.append(parts.copy())
                return
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                parts.append(nums[j])
                dfs(j + 1, size)
                parts.pop()

        for s in range(n + 1):
            dfs(0, s)
        return res



        
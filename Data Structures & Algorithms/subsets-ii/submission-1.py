class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        parts = []
        def dfs(i):
            res.append(parts.copy())
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                parts.append(nums[j])
                dfs(j + 1)
                parts.pop()

        dfs(0)
        return res



        
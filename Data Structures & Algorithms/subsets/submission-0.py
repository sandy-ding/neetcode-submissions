class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(arr, i):
            if i == len(nums):
                result.append(arr[:])
                return
            backtrack(arr, i + 1)
            arr.append(nums[i])
            backtrack(arr, i + 1)
            arr.pop()

        backtrack([], 0)
        return result
        
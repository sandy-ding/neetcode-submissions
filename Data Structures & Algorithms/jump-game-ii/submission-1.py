class Solution:
    def jump(self, nums: List[int]) -> int:
        step, i = 0, 0

        while i < len(nums) - 1:
            step += 1
            max_index = i + nums[i]
            temp = max_index
            if max_index < len(nums) - 1:
                for j in range(i + 1, min(len(nums), max_index + 1)):
                    if j + nums[j] > max_index:
                        max_index = max(max_index, j + nums[j])
                        temp = j
                i = temp
            else:
                break

        return step
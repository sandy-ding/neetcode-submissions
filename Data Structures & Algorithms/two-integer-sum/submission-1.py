class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in map_:
                return [map_[diff], i]
            map_[num] = i
        return []
        
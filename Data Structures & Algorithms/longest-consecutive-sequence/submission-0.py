class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                len_ = 1
                while (num + len_) in numSet:
                    len_ += 1
                longest = max(longest, len_)
        return longest
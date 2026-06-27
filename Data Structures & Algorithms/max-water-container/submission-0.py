class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_ = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_ = max(max_, area)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1

        return max_
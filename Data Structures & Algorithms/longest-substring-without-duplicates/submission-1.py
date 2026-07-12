class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        indexMap = {}
        longest = 0

        while right < len(s):
            if s[right] in indexMap:
                left = max(indexMap[s[right]] + 1, left)
            indexMap[s[right]] = right
            longest = max(longest, right - left + 1)
            right += 1

        return longest
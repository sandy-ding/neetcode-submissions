class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_leng_left, max_leng_right = 0, 0
        for i in range(len(s)):
            for left, right in [(i, i), (i, i + 1)]:
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left > max_leng_right - max_leng_left:
                        max_leng_left = left
                        max_leng_right = right
                    left -= 1
                    right += 1
        return s[max_leng_left:max_leng_right + 1]
                    

        
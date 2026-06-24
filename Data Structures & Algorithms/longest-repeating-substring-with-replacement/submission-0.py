class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start = 0
        res = 0
        max_frequency = 0

        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            max_frequency = max(max_frequency, count[s[end]])

            while end - start + 1 - max_frequency > k:
                count[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)

        return res
        


        
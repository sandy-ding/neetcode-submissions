class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = defaultdict(int)
        map_t = defaultdict(int)

        for ch in s:
            map_s[ch] += 1
        
        for ch in t:
            map_t[ch] += 1

        return map_s == map_t
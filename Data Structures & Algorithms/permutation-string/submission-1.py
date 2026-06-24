class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target_map = defaultdict(int)

        for ch in s1:
            target_map[ch] += 1

        hash_map = defaultdict(int)
        for i in range(len(s2)): 
            hash_map[s2[i]] += 1
            if i >= len(s1):
                hash_map[s2[i - len(s1)]] -= 1
                if hash_map[s2[i - len(s1)]] == 0:
                    del hash_map[s2[i - len(s1)]]
            
            if hash_map == target_map:
                return True

        return False

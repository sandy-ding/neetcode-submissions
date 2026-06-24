class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hash_map = { 0: 0 }

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin in hash_map:
                    hash_map[i] = min(hash_map[i - coin] + 1, hash_map[i]) if i in hash_map else hash_map[i - coin] + 1

        return hash_map[amount] if amount in hash_map else -1
            
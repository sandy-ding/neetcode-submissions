class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        arr = [-math.inf] * (len(prices) - 1)
        arr[-1] = prices[-1]
        for i in range(len(arr) - 2, -1, -1):
            arr[i] = max(arr[i + 1], prices[i + 1])

        max_ = -math.inf
        for i in range(len(arr)):
            max_ = max(max_, arr[i] - prices[i])

        return max_ if max_ > 0 else 0
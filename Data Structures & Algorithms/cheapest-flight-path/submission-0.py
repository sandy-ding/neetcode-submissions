class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float("inf")] * n
        price[src] = 0

        for i in range(k + 1):
            temp = price.copy()

            for s, e, p in flights:
                if price[s] == float("inf"):
                    continue
                if price[s] + p < temp[e]:
                    temp[e] = price[s] + p
            price = temp

        return price[dst] if price[dst] != float("inf") else -1

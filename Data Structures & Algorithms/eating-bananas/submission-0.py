class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalHour(speed):
            total_hour = 0
            for pile in piles:
                total_hour += math.ceil(pile / speed) 
            return total_hour

        right = max(piles)
        left = 1
        while left < right:
            mid = (left + right) // 2
            if totalHour(mid) <= h:
                right = mid
            else:
                left = mid + 1
        
        return right


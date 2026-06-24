class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n

        while cur != 1:
            temp = 0
            while cur > 0:
                temp += (cur % 10) ** 2
                cur //= 10
            if temp in seen:
                return False
            seen.add(temp)
            cur = temp

        return True

    
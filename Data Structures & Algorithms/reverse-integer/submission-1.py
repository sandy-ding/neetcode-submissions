class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1 if x > 0 else -1
        x *= sign
        while x != 0:
            digit = x % 10
            x = x // 10
            
            if res > 214748364 or (res == 214748364 and x % 10 > 7):
                return 0
            
            res = res * 10 + digit
            
        return res * sign
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        map_ = {"0": 0, "1": 1, "2": 2, "3":3, "4":4, "5":5,
            "6": 6, "7": 7, "8": 8, "9": 9}
        n1, n2 = 0, 0
        for ch in num1:
            n1 *= 10
            n = map_[ch]
            n1 += n

        for ch in num2:
            n2 *= 10
            n = map_[ch]
            n2 += n

        num = n1 * n2
        return str(num)
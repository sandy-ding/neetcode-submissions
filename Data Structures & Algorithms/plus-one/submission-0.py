class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur = 1
        for i in range(len(digits) - 1, -1, -1):
            _sum = cur + digits[i]
            digits[i] = _sum % 10
            cur = _sum // 10
        if cur != 0:
            digits.insert(0, cur)
        return digits
        
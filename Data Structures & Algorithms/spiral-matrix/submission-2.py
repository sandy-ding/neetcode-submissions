class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 0
        ROW, COL = len(matrix), len(matrix[0])
        res = []
        top, bottom = 0, ROW - 1
        left, right = 0, COL - 1

        while len(res) != ROW * COL:
            if direction % 4 == 0:
                for c in range(left, right + 1):
                    res.append(matrix[top][c])
            elif direction % 4 == 1:
                for r in range(top + 1, bottom + 1):
                    res.append(matrix[r][right])
            elif direction % 4 == 2:
                for c in range(right - 1, left, -1):
                    res.append(matrix[bottom][c])
            elif direction % 4 == 3:
                for r in range(bottom, top, -1):
                    res.append(matrix[r][left])
                left += 1
                right -= 1
                top += 1
                bottom -= 1
            direction += 1
        return res

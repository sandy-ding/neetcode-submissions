class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS - r):
                matrix[r][c], matrix[ROWS - 1 - c][COLS - 1 - r] = matrix[ROWS - 1 - c][COLS - 1 - r], matrix[r][c]

        for r in range(ROWS // 2):
            for c in range(COLS):
                matrix[r][c], matrix[ROWS - 1 - r][c] = matrix[ROWS - 1 - r][c], matrix[r][c]
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroInFirstRow, zeroInFirstCol = False, False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    if r == 0:
                        zeroInFirstRow = True
                    if c == 0:
                        zeroInFirstCol = True
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0
        
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(len(matrix)):
                    matrix[r][c] = 0

        if zeroInFirstRow:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0

        if zeroInFirstCol:
            for r in range(len(matrix)):
                matrix[r][0] = 0
    
        
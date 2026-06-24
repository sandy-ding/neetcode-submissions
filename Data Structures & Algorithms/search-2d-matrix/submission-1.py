class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        lrow, rrow = 0, ROW - 1
        lcol, rcol = 0, COL - 1

        while lrow * COL + lcol <= rrow * COL + rcol:
            mid = (rrow * COL + rcol + lrow * COL + lcol) // 2
            mrow = mid // COL
            mcol = mid % COL
            if matrix[mrow][mcol] < target:
                lower = mid + 1
                lrow = lower // COL
                lcol = lower % COL
            elif matrix[mrow][mcol] > target:
                higher = mid - 1
                rrow = higher // COL
                rcol = higher % COL
            else:
                return True
        return False

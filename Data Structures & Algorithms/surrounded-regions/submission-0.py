class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if row < 0 or row == ROW or col < 0 or col == COL or board[row][col] != "O":
                return
            board[row][col] = "#"
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                dfs(nr, nc)

        for r in range(ROW):
            for c in range(COL):
                if r == 0 or r == ROW - 1 or c == 0 or c == COL - 1:
                    dfs(r, c)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
            



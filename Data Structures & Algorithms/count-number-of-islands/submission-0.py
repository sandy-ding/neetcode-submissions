class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    num += 1
                    q.append((row, col))
                    grid[row][col] = "0"

                    while q:
                        r, c = q.pop()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                q.append((nr, nc))

        return num
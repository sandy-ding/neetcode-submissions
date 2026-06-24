class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                q = []
                area = 0
                if grid[r][c] == 1:
                    q.append((r, c))
                    grid[r][c] = 2
                while q:
                    row, col = q.pop(0)
                    area += 1
                    max_area = max(area, max_area)
                    for dr, dc in directions:
                        nr = row + dr
                        nc = col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))

        return max_area


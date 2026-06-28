class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visited = set()
        q = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        distance = 0
        while q:
            len_ = len(q)
            distance += 1
            for i in range(len_):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] > 0 and (nr, nc) not in visited:
                        grid[nr][nc] = distance
                        q.append((nr, nc))
                        visited.add((nr, nc))

    
            
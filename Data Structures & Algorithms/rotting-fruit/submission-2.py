class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        freshFruit= 0

        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    freshFruit += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        if freshFruit == 0:
            return time
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            len_ = len(queue)
            for i in range(len_):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        freshFruit -= 1
            time += 1
        return -1 if freshFruit > 0 else time - 1



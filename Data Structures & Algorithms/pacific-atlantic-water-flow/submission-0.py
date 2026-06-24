class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        visited = set()

        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        rows, cols = len(heights), len(heights[0])
        nodes = [(i, 0) for i in range(rows)] + [(0, i) for i in range(1, cols)]
        while nodes:
            r, c = nodes.pop(0)
            pac.add((r, c))
            visited.add((r, c))
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0<= row < rows and 0 <= col < cols and heights[row][col] >= heights[r][c] and (row, col) not in visited:
                    nodes.append((row, col))

        nodes = [(i, cols - 1) for i in range(rows)] + [(rows - 1, i) for i in range(cols - 1)]
        visited = set()
        while nodes:
            r, c = nodes.pop(0)
            atl.add((r, c))
            visited.add((r, c))
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0<= row < rows and 0 <= col < cols and heights[row][col] >= heights[r][c] and (row, col) not in visited:
                    nodes.append((row, col))

        return list(pac.intersection(atl))
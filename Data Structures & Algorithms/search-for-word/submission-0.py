class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def dfs(r, c, index, visited):
            if index == len(word):
                return True

            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and board[r][c] == word[index]:
                visited.add((r, c))
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if dfs(nr, nc, index + 1, visited):
                        return True
                visited.remove((r, c))

            return False


        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0, set()):
                    return True
        
        return False


        
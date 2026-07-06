class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj = defaultdict(list)
        visited = set()

        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for nei in adj[n]:
                dfs(nei)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1

        return res
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        queue = deque([(0, -1)])
        visited = set()
        visited.add(0)
        while queue:
            node, parent = queue.popleft()
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                queue.append((nei, node))
                visited.add(nei)

        return len(visited) == n
            
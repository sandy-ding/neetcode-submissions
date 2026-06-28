class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        len_ = len(edges)
        indegrees = [0] * (len_ + 1)
        adj = [[] for _ in range(len_ + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegrees[u] += 1
            indegrees[v] += 1

        q = deque()
        for i in range(1, len_ + 1):
            if indegrees[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            indegrees[node] -= 1
            for nei in adj[node]:
                indegrees[nei] -= 1  
                if indegrees[nei] == 1:
                    q.append(nei)

        for u, v in reversed(edges):
            if indegrees[u] > 0 and indegrees[v] > 0:
                return [u, v]

        return []
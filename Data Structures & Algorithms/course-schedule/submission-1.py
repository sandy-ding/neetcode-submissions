class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { key: [] for key in range(numCourses) }
        UNVISITED, VISITING, DONE = 0, 1, 2
        state = [UNVISITED] * numCourses
        for u, v in prerequisites:
            adj[v].append(u)

        def hasCircle(n):
            if state[n] == VISITING:
                return True
            if state[n] == DONE:
                return False
            state[n] = VISITING
            for nei in adj[n]:
                if hasCircle(nei):
                    return True
            state[n] = DONE
            return False
                
        for node in adj:
            if hasCircle(node):
                return False
        return True

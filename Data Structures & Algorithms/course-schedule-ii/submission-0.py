class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = defaultdict(list)
        indegree = defaultdict(int)
        res = []

        for child, pre in prerequisites:
            pre_map[pre].append(child)
            indegree[child] += 1
            if pre not in indegree:
                indegree[pre] = 0
        
        q = deque()
        for key, value in indegree.items():
            if value == 0:
                q.append(key)

        while q:
            key = q.pop()
            res.append(key)
            for child in pre_map[key]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)

        for key, value in indegree.items():
            if value > 0:
                return []

        for i in range(numCourses):
            if i not in res:
                res.append(i)

        return res

        
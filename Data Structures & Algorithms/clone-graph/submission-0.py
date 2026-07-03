"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hash_map = { node: Node(node.val) }
        q = deque([node])
        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei not in hash_map:
                    hash_map[nei] = Node(nei.val)
                    q.append(nei)
                hash_map[n].neighbors.append(hash_map[nei])
        return hash_map[node]

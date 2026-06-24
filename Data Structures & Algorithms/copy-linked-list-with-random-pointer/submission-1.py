"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {}
        dump_head = Node(0, None, None)
        pointer = dump_head
        pointer_head = head

        while pointer_head:
            node = Node(pointer_head.val, None, None)
            hash_map[pointer_head] = node
            pointer.next = node
            pointer = pointer.next
            pointer_head = pointer_head.next

        pointer = dump_head.next
        pointer_head = head

        while pointer_head:
            if pointer_head.random:
                pointer.random = hash_map[pointer_head.random]
            pointer_head = pointer_head.next
            pointer = pointer.next

        return dump_head.next


        
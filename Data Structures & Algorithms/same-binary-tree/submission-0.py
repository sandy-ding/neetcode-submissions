# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = [p]
        queue2 = [q]
        while queue1 and queue2:
            p_node = queue1.pop()
            q_node = queue2.pop()
            if not p_node and not q_node:
                 continue
            if not q_node or not p_node or p_node.val != q_node.val:
                return False

            queue1.append(p_node.left)
            queue1.append(p_node.right)
            queue2.append(q_node.left)
            queue2.append(q_node.right)

        return len(queue1) == len(queue2)
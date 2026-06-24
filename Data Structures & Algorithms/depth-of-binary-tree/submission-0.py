# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        arr = [root]
        depth = 0
        while arr:
            depth += 1
            for i in range(len(arr)):
                node = arr.pop(0)
                if node.left:
                    arr.append(node.left)
                if node.right:
                    arr.append(node.right)

        return depth


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node, depth):
            nonlocal diameter
            if node is None:
                return depth
            
            left = dfs(node.left, 0)
            right = dfs(node.right, 0)
            diameter = max(diameter, left + right)
            return max(left, right) + 1


        dfs(root, 0)
        return diameter
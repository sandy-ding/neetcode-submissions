# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        
        def dfs(node, depth):
            nonlocal isBalanced
            if not node:
                return depth
            
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            if abs(left - right) > 1:
                isBalanced = False
            return max(left, right)
        
        dfs(root, 0)
        return isBalanced

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def maxRob(node):
            if not node:
                return 0
            if node in cache:
                return cache[node]
            dont_rob = maxRob(node.left)+maxRob(node.right)
            rob_curr = node.val
            if node.left:
                rob_curr+=maxRob(node.left.left)+maxRob(node.left.right)
            if node.right:
                rob_curr+=maxRob(node.right.left)+maxRob(node.right.right)
            cache[node] = max(dont_rob,rob_curr)
            return cache[node]
        return maxRob(root)
            
        
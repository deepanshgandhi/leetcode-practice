# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [root]
        def lca(root):
            if root is None:
                return False
            left = lca(root.left)
            right = lca(root.right)
            if left and right:
                res[0] = root
            if (left or right) and (root.val == p.val or root.val == q.val):
                res[0] = root
            return root.val==p.val or root.val==q.val or left or right
        lca(root)
        return res[0]
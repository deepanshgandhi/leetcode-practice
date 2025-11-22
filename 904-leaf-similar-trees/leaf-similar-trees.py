# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root,result):
            if root is None:
                return
            if not root.left and not root.right:
                result.append(root.val)
                return
            leaves(root.left,result)
            leaves(root.right,result)
        l1,l2=[],[]
        leaves(root1,l1)
        leaves(root2,l2)
        print(l1,l2)
        return l1==l2
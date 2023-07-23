# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both trees are null return true
        if not p and not q:
            return True
        # if either of the tree is null or the value on the same position not same return False
        if not p or not q or p.val != q.val:
            return False
        # recurse both the left and right while comparing the lefts with the lefts and rights with the rights
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
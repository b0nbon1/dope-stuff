# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        # go through the tree
        while curr:
            # if the both p and q are greater than curr subtree parent go the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # if the both p and q are less than curr subtree parent go the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # else pick the parent and return as the least common ancestor
            else:
                return curr
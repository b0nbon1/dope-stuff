# https://leetcode.com/problems/subtree-of-another-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base when no root and subtree meaning they are both the same
        if not root and not subRoot:
            return True
        # when no root but there is subtree, subtree does not exists
        if not root:
            return False
        
        # check if current root is similar to subtree, return true
        if self.isSameTree(root, subRoot):
            return True
        # otherwise recurse on the nodes
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

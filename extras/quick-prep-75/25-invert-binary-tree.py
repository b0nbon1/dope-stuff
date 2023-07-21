# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case, if not root stop here 
        if not root:
            return None
        # switch the left node to go to the right and vice verse while inverting the tree
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root once done
        return root
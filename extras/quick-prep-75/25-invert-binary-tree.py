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
        # swap the left node to go to the right and vice verse while inverting the tree
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        # return root once done
        return root
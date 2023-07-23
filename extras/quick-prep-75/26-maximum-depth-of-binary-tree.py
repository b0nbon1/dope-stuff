# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if no root means there are no nodes return 0
        if not root:
            return 0
        # compare between the length of the left nodes and right node. which ones has the longest height
        maxDepthVal = max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))
        # return the max depth
        return maxDepthVal
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
      if not root: return float("-inf")
      res = [root.val]
      def dfs(root):
        if not root:
          return 0
        leftMax = max(self.dfs(root.left), 0)
        rightMax = max(self.dfs(root.right), 0)

        res[0] = max(res[0], root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)
      dfs(root)
      return res[0]
        
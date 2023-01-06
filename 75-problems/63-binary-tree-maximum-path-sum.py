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

    
    # class Solution:
		# 				def isBalanced(self, root: Optional[TreeNode]) -> bool:

		# 					def height(root):
		# 						if not root:
		# 							return 0

		# 						left=height(root.left)
		# 						right=height(root.right)

		# 						if abs(left-right)>1:
		# 							res[0]=False
		# 						return 1+ max(left,right)

		# 					res=[True]
		# 					height(root)
		# 					return res[0]

    # class Solution():
    #   def isBalanced(self, root):
    #       return (self.Height(root) >= 0)
    #   def Height(self, root):
    #       if root is None:  return 0
    #       leftheight, rightheight = self.Height(root.left), self.Height(root.right)
    #       if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
    #       return max(leftheight, rightheight) + 1
        
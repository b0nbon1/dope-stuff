class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
      result = []
      if not root: return 0
      queue = [root]
      while queue:
        level_sum = 0
        n = len(queue)
        for i in range(n):
          current = queue.pop(0)
          level_sum += current.val
          if current.right: queue.append(current.right)
          if current.left: queue.append(current.left)
        result.append(level_sum/n)
      return result
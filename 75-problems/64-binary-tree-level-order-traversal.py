from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if not root: return []
      res = []
      queue = deque([root])
      while queue:
        currentArr = []
        n = len(queue)
        for i in range(n):
          current = queue.popleft()
          
          currentArr.append(current.val)
          if current.left: queue.append(current.left)
          if current.right: queue.append(current.right)
        res.append(currentArr)
      return res 
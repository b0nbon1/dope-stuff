from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs
class Solutiondfs1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(tree, depth):
          if not tree: return depth
          return max(dfs(tree.left, depth+1), dfs(tree.right, depth+1))
        return dfs(root, 0)

class Solutiondfs2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#bfs
class Solutionbfs:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      if not root: return 0
      level = 0
      q = deque([root])
      while q:
        for i in range(len(q)):
          node = q.popleft()
          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)
        level+=1
      return level

# dfs iterative
class Solutiondfsiter:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      stack = [[root, 1]]
      res = 0
      while stack:
        node, depth = stack.pop()
        if node:
          res = max(res, depth)
          stack.append([node.left, depth+1])
          stack.append([node.right, depth+1])
      return res

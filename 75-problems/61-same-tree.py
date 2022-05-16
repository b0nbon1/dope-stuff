# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs stacks
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if not q and not p:
        return True
      if not q or not p:
        return False
      stackP = [p]
      stackQ = [q]
      while stackP and stackQ:
        currentP = stackP.pop()
        currentQ = stackQ.pop()
        Pval = currentP.val if currentP else None
        Qval = currentQ.val if currentQ else None
        if Pval != Qval:
          return False
        if Qval is not None:
          stackQ.append(currentQ.left)
          stackQ.append(currentQ.right)
        if Pval is not None:
          stackP.append(currentP.left)
          stackP.append(currentP.right)

        
      if stackP or stackQ:
        return False
      return True

# dfs stacks
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if not p and not q:
        return True
      if not p or not q or p.val != q.val:
        return False
      return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

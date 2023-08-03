from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        q = deque()
        if root:
            q.append(root)
        result = []
        while q:
            values = []
            length = len(q)
            for i in range(length):
                child = q.popleft()
                values.append(child.val)
                if child.left:
                    q.append(child.left)
                if child.right:
                    q.append(child.right)
            result.append(values)
        return result


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
tree.left.left = TreeNode(12)
tree.left.right = TreeNode(6)

sol = Solution()
sol.levelOrder(tree)


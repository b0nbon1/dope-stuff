from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        # we can solve this using bfs and queues
        q = deque()
        # if there is root, append to a queue
        if root:
            q.append(root)
        # this will store our results
        result = []
        # while there is something in the queue, keep looping
        while q:
            # this will store values on that level
            values = []
            # get the length of the current level of a tree
            length = len(q)
            # loop through the level while popping out the children
            for i in range(length):
                # get the child
                child = q.popleft()
                #  add the child to curr level list
                values.append(child.val)
                # if the child has left child, add it to queue
                if child.left:
                    q.append(child.left)
                # if the child has right child, add it to queue
                if child.right:
                    q.append(child.right)
            # after traversing through the level add the values to the result list
            result.append(values)
        # return the result
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

